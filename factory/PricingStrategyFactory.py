"""
package org.nailyourinterview.lld.parking_lot.factory;

import org.nailyourinterview.lld.parking_lot.enums.PricingStrategyType;
import org.nailyourinterview.lld.parking_lot.strategy.pricing.*;

public class PricingStrategyFactory {
    public static PricingStrategy get(PricingStrategyType type) {
        return switch (type) {
            case TIME_BASED -> new TimeBasedPricing();
            case EVENT_BASED -> new EventBasedPricing();
        };
    }
}
"""

from enums.PricingStrategyType import PricingStrategyType
from strategy.pricing.PricingStrategy import PricingStrategy
from strategy.pricing.TimeBasedPricing import TimeBasedPricing
from strategy.pricing.EventBasedPricing import EventBasedPricing

class PricingStrategyFactory:
    @staticmethod
    def get(type: PricingStrategyType) -> PricingStrategy:
        match type:
            case PricingStrategyType.TIME_BASED:
                return TimeBasedPricing()
            case PricingStrategyType.EVENT_BASED:
                return EventBasedPricing()
            case _:
                raise ValueError(f"Invalid pricing strategy type: {type}")
