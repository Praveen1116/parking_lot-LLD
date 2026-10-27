"""
package org.nailyourinterview.lld.parking_lot.service;

import lombok.Getter;
import lombok.Setter;
import org.nailyourinterview.lld.parking_lot.enums.PaymentMode;
import org.nailyourinterview.lld.parking_lot.enums.*;
import org.nailyourinterview.lld.parking_lot.factory.*;
import org.nailyourinterview.lld.parking_lot.model.*;
import org.nailyourinterview.lld.parking_lot.strategy.payment.*;
import org.nailyourinterview.lld.parking_lot.strategy.pricing.*;

import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

@Getter
public class ParkingLot {
    private static final ParkingLot INSTANCE = new ParkingLot();

    private final Map<String, ParkingFloor> floors = new HashMap<>();
    private final Map<String, Ticket> activeTickets = new HashMap<>();
    @Setter
    private PricingStrategy pricingStrategy;

    private ParkingLot() {
        this.pricingStrategy = PricingStrategyFactory.get(PricingStrategyType.TIME_BASED);
    }

    public static ParkingLot getInstance() {
        return INSTANCE;
    }

    public void addFloor(ParkingFloor floor) {
        floors.put(floor.getId(), floor);
    }

    // b1, b2 (one spot)
    // car, bike

    public Ticket parkVehicle(Vehicle vehicle, LocalDateTime entryTime) {
        for (ParkingFloor floor : floors.values()) {
            ParkingSpot spot = floor.findAvailableSpot(vehicle.getType());

            if (spot != null) {
                // Successfully reserved the spot via atomic operation
                String ticketId = UUID.randomUUID().toString();
                Ticket ticket = Ticket.builder()
                        .ticketId(ticketId)
                        .entryTime(entryTime)
                        .vehicle(vehicle)
                        .floorId(floor.getId())
                        .spotId(spot.getId())
                        .build();

                activeTickets.put(ticketId, ticket);
                System.out.println("Vehicle parked. Ticket: " + ticketId);
                return ticket;
            }
        }

        System.out.println("No spot available for vehicle type: " + vehicle.getType());
        return null;
    }

    public void unparkVehicle(String ticketId, LocalDateTime exitTime, PaymentMode paymentMode) {
        Ticket ticket = activeTickets.get(ticketId);
        if (ticket == null) {
            System.out.println("Invalid ticket ID.");
            return;
        }

        double fee = pricingStrategy.calculateFee(
                ticket.getVehicle().getType(),
                ticket.getEntryTime(),
                exitTime
        );

        PaymentStrategy strategy = PaymentStrategyFactory.get(paymentMode);
        PaymentProcessor processor = new PaymentProcessor(strategy);
        boolean paid = processor.pay(ticket, fee);

        if (!paid) {
            System.out.println("Vehicle cannot exit. Payment unsuccessful.");
            return;
        }

        ParkingSpot spot = floors.get(ticket.getFloorId()).getSpots().get(ticket.getSpotId());
        spot.vacate();
        activeTickets.remove(ticketId);

        System.out.println("Vehicle exited. Fee charged: ₹" + fee);
    }

    public void printStatus() {
        floors.forEach((floorId, floor) -> {
            System.out.println("Floor: " + floorId);
            floor.getSpots().values().forEach(spot -> {
                System.out.println(" Spot " + spot.getId() + " [" + spot.getAllowedType() + "] - " + (spot.isOccupied() ? "Occupied" : "Free"));
            });
        });
    }
}
"""

from typing import Dict, Optional, Any
from datetime import datetime
import uuid

from enums.PaymentMode import PaymentMode
from model.Vehicle import Vehicle
from model.ParkingFloor import ParkingFloor
from model.ParkingSpot import ParkingSpot
from model.Ticket import Ticket

try:
    from strategy.pricing.PricingStrategy import PricingStrategy
except (ImportError, AttributeError):
    PricingStrategy = object  # type: ignore

class ParkingLot:
    _instance: Optional["ParkingLot"] = None

    def __init__(self):
        self.floors: Dict[str, ParkingFloor] = {}
        self.activeTickets: Dict[str, Ticket] = {}
        self.pricingStrategy: Optional[Any] = None
        try:
            from factory.PricingStrategyFactory import PricingStrategyFactory
            from enums.PricingStrategyType import PricingStrategyType
            self.pricingStrategy = PricingStrategyFactory.get(PricingStrategyType.TIME_BASED)
        except (ImportError, AttributeError):
            self.pricingStrategy = None

    @classmethod
    def getInstance(cls) -> "ParkingLot":
        if cls._instance is None:
            cls._instance = ParkingLot()
        return cls._instance

    def getFloors(self) -> Dict[str, ParkingFloor]:
        return self.floors

    def getActiveTickets(self) -> Dict[str, Ticket]:
        return self.activeTickets

    def getPricingStrategy(self) -> Optional[Any]:
        return self.pricingStrategy

    def setPricingStrategy(self, pricingStrategy: Any) -> None:
        self.pricingStrategy = pricingStrategy

    def addFloor(self, floor: ParkingFloor) -> None:
        self.floors[floor.getId()] = floor

    def parkVehicle(self, vehicle: Vehicle, entryTime: datetime) -> Optional[Ticket]:
        for floor in self.floors.values():
            spot = floor.findAvailableSpot(vehicle.getType())

            if spot is not None:
                ticketId = str(uuid.uuid4())
                ticket = (
                    Ticket.builder()
                    .ticketId(ticketId)
                    .entryTime(entryTime)
                    .vehicle(vehicle)
                    .floorId(floor.getId())
                    .spotId(spot.getId())
                    .build()
                )
                self.activeTickets[ticketId] = ticket
                print(f"Vehicle parked. Ticket: {ticketId}")
                return ticket

        print(f"No spot available for vehicle type: {vehicle.getType()}")
        return None

    def unparkVehicle(self, ticketId: str, exitTime: datetime, paymentMode: PaymentMode) -> None:
        ticket = self.activeTickets.get(ticketId)
        if ticket is None:
            print("Invalid ticket ID.")
            return

        if self.pricingStrategy is None:
            print("Pricing strategy not configured.")
            return

        fee = self.pricingStrategy.calculateFee(
            ticket.getVehicle().getType(),
            ticket.getEntryTime(),
            exitTime
        )

        from factory.PaymentStrategyFactory import PaymentStrategyFactory
        from service.PaymentProcessor import PaymentProcessor

        strategy = PaymentStrategyFactory.get(paymentMode)
        processor = PaymentProcessor(strategy)
        paid = processor.pay(ticket, fee)

        if not paid:
            print("Vehicle cannot exit. Payment unsuccessful.")
            return

        floor = self.floors.get(ticket.getFloorId())
        if floor:
            spot = floor.getSpots().get(ticket.getSpotId())
            if spot:
                spot.vacate()

        del self.activeTickets[ticketId]
        print(f"Vehicle exited. Fee charged: ₹{fee}")

    def printStatus(self) -> None:
        for floorId, floor in self.floors.items():
            print(f"Floor: {floorId}")
            for spot in floor.getSpots().values():
                status = "Occupied" if spot.isOccupied() else "Free"
                print(f" Spot {spot.getId()} [{spot.getAllowedType()}] - {status}")
