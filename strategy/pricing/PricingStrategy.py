"""
package org.nailyourinterview.lld.parking_lot.strategy.pricing;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.time.LocalDateTime;

public interface PricingStrategy {
    double calculateFee(VehicleType type, LocalDateTime entryTime, LocalDateTime exitTime);
}
"""

from abc import ABC, abstractmethod
from datetime import datetime
from enums.VehicleType import VehicleType

class PricingStrategy(ABC):
    @abstractmethod
    def calculateFee(self, type: VehicleType, entryTime: datetime, exitTime: datetime) -> float:
        pass
