from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .approval_solution import ApprovalSolution
    from .backup_restore_root import BackupRestoreRoot
    from .booking_business import BookingBusiness
    from .booking_currency import BookingCurrency
    from .business_scenario import BusinessScenario
    from .virtual_events_root import VirtualEventsRoot

@dataclass
class SolutionsRoot(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The approval property
    approval: Optional[ApprovalSolution] = None
    # The backupRestore property
    backup_restore: Optional[BackupRestoreRoot] = None
    # A collection of businesses in Microsoft Bookings. Read-only. Nullable.
    booking_businesses: Optional[list[BookingBusiness]] = None
    # A collection of monetary currencies supported by a bookingBusiness. Read-only. Nullable.
    booking_currencies: Optional[list[BookingCurrency]] = None
    # A collection of scenarios that contain relevant data and configuration information for a specific problem domain.
    business_scenarios: Optional[list[BusinessScenario]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of virtual events.
    virtual_events: Optional[VirtualEventsRoot] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SolutionsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SolutionsRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SolutionsRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .approval_solution import ApprovalSolution
        from .backup_restore_root import BackupRestoreRoot
        from .booking_business import BookingBusiness
        from .booking_currency import BookingCurrency
        from .business_scenario import BusinessScenario
        from .virtual_events_root import VirtualEventsRoot

        from .approval_solution import ApprovalSolution
        from .backup_restore_root import BackupRestoreRoot
        from .booking_business import BookingBusiness
        from .booking_currency import BookingCurrency
        from .business_scenario import BusinessScenario
        from .virtual_events_root import VirtualEventsRoot

        fields: dict[str, Callable[[Any], None]] = {
            "approval": lambda n : setattr(self, 'approval', n.get_object_value(ApprovalSolution)),
            "backupRestore": lambda n : setattr(self, 'backup_restore', n.get_object_value(BackupRestoreRoot)),
            "bookingBusinesses": lambda n : setattr(self, 'booking_businesses', n.get_collection_of_object_values(BookingBusiness)),
            "bookingCurrencies": lambda n : setattr(self, 'booking_currencies', n.get_collection_of_object_values(BookingCurrency)),
            "businessScenarios": lambda n : setattr(self, 'business_scenarios', n.get_collection_of_object_values(BusinessScenario)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "virtualEvents": lambda n : setattr(self, 'virtual_events', n.get_object_value(VirtualEventsRoot)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("approval", self.approval)
        writer.write_object_value("backupRestore", self.backup_restore)
        writer.write_collection_of_object_values("bookingBusinesses", self.booking_businesses)
        writer.write_collection_of_object_values("bookingCurrencies", self.booking_currencies)
        writer.write_collection_of_object_values("businessScenarios", self.business_scenarios)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("virtualEvents", self.virtual_events)
        writer.write_additional_data_value(self.additional_data)
    

