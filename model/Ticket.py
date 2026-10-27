"""
package org.nailyourinterview.lld.parking_lot.model;

import lombok.Builder;
import lombok.Data;
import org.nailyourinterview.lld.parking_lot.enums.PaymentStatus;

import java.time.LocalDateTime;

@Data
@Builder
public class Ticket {
    private String ticketId;
    private LocalDateTime entryTime;
    private Vehicle vehicle;
    private String floorId;
    private String spotId;
    private PaymentStatus paymentStatus = PaymentStatus.PENDING;
}
"""

from datetime import datetime
from typing import Optional
from enums.PaymentStatus import PaymentStatus
from model.Vehicle import Vehicle

class Ticket:
    def __init__(
        self,
        ticketId: str = "",
        entryTime: Optional[datetime] = None,
        vehicle: Optional[Vehicle] = None,
        floorId: str = "",
        spotId: str = "",
        paymentStatus: PaymentStatus = PaymentStatus.PENDING
    ):
        self.ticketId = ticketId
        self.entryTime = entryTime
        self.vehicle = vehicle
        self.floorId = floorId
        self.spotId = spotId
        self.paymentStatus = paymentStatus

    def getTicketId(self) -> str:
        return self.ticketId

    def getEntryTime(self) -> Optional[datetime]:
        return self.entryTime

    def getVehicle(self) -> Optional[Vehicle]:
        return self.vehicle

    def getFloorId(self) -> str:
        return self.floorId

    def getSpotId(self) -> str:
        return self.spotId

    def getPaymentStatus(self) -> PaymentStatus:
        return self.paymentStatus

    def setPaymentStatus(self, paymentStatus: PaymentStatus) -> None:
        self.paymentStatus = paymentStatus

    @classmethod
    def builder(cls):
        class Builder:
            def __init__(self):
                self._ticketId: str = ""
                self._entryTime: Optional[datetime] = None
                self._vehicle: Optional[Vehicle] = None
                self._floorId: str = ""
                self._spotId: str = ""
                self._paymentStatus: PaymentStatus = PaymentStatus.PENDING

            def ticketId(self, ticketId: str):
                self._ticketId = ticketId
                return self

            def entryTime(self, entryTime: datetime):
                self._entryTime = entryTime
                return self

            def vehicle(self, vehicle: Vehicle):
                self._vehicle = vehicle
                return self

            def floorId(self, floorId: str):
                self._floorId = floorId
                return self

            def spotId(self, spotId: str):
                self._spotId = spotId
                return self

            def paymentStatus(self, paymentStatus: PaymentStatus):
                self._paymentStatus = paymentStatus
                return self

            def build(self) -> "Ticket":
                return Ticket(
                    ticketId=self._ticketId,
                    entryTime=self._entryTime,
                    vehicle=self._vehicle,
                    floorId=self._floorId,
                    spotId=self._spotId,
                    paymentStatus=self._paymentStatus
                )

        return Builder()
from enums.PaymentStatus import PaymentStatus
from model.Vehicle import Vehicle

class Ticket:
    def __init__(
        self,
        ticketId: str = "",
        entryTime: Optional[datetime] = None,
        vehicle: Optional[Vehicle] = None,
        floorId: str = "",
        spotId: str = "",
        paymentStatus: PaymentStatus = PaymentStatus.PENDING
    ):
        self.ticketId = ticketId
        self.entryTime = entryTime
        self.vehicle = vehicle
        self.floorId = floorId
        self.spotId = spotId
        self.paymentStatus = paymentStatus

    def getTicketId(self) -> str:
        return self.ticketId

    def getEntryTime(self) -> Optional[datetime]:
        return self.entryTime

    def getVehicle(self) -> Optional[Vehicle]:
        return self.vehicle

    def getFloorId(self) -> str:
        return self.floorId

    def getSpotId(self) -> str:
        return self.spotId

    def getPaymentStatus(self) -> PaymentStatus:
        return self.paymentStatus

    def setPaymentStatus(self, paymentStatus: PaymentStatus) -> None:
        self.paymentStatus = paymentStatus

    @classmethod
    def builder(cls):
        class Builder:
            def __init__(self):
                self._ticketId: str = ""
                self._entryTime: Optional[datetime] = None
                self._vehicle: Optional[Vehicle] = None
                self._floorId: str = ""
                self._spotId: str = ""
                self._paymentStatus: PaymentStatus = PaymentStatus.PENDING

            def ticketId(self, ticketId: str):
                self._ticketId = ticketId
                return self

            def entryTime(self, entryTime: datetime):
                self._entryTime = entryTime
                return self

            def vehicle(self, vehicle: Vehicle):
                self._vehicle = vehicle
                return self

            def floorId(self, floorId: str):
                self._floorId = floorId
                return self

            def spotId(self, spotId: str):
                self._spotId = spotId
                return self

            def paymentStatus(self, paymentStatus: PaymentStatus):
                self._paymentStatus = paymentStatus
                return self

            def build(self) -> "Ticket":
                return Ticket(
                    ticketId=self._ticketId,
                    entryTime=self._entryTime,
                    vehicle=self._vehicle,
                    floorId=self._floorId,
                    spotId=self._spotId,
                    paymentStatus=self._paymentStatus
                )

        return Builder()
from typing import Optional
