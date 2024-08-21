from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ComanagementEligibleDevicesSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Count of devices already Co-Managed
    comanaged_count: Optional[int] = None
    # Count of devices eligible for Co-Management but not yet joined to Azure Active Directory
    eligible_but_not_azure_ad_joined_count: Optional[int] = None
    # Count of devices fully eligible for Co-Management
    eligible_count: Optional[int] = None
    # Count of devices ineligible for Co-Management
    ineligible_count: Optional[int] = None
    # Count of devices that will be eligible for Co-Management after an OS update
    needs_os_update_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Count of devices scheduled for Co-Management enrollment. Valid values 0 to 9999999
    scheduled_for_enrollment_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ComanagementEligibleDevicesSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComanagementEligibleDevicesSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ComanagementEligibleDevicesSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "comanagedCount": lambda n : setattr(self, 'comanaged_count', n.get_int_value()),
            "eligibleButNotAzureAdJoinedCount": lambda n : setattr(self, 'eligible_but_not_azure_ad_joined_count', n.get_int_value()),
            "eligibleCount": lambda n : setattr(self, 'eligible_count', n.get_int_value()),
            "ineligibleCount": lambda n : setattr(self, 'ineligible_count', n.get_int_value()),
            "needsOsUpdateCount": lambda n : setattr(self, 'needs_os_update_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scheduledForEnrollmentCount": lambda n : setattr(self, 'scheduled_for_enrollment_count', n.get_int_value()),
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
        writer.write_int_value("comanagedCount", self.comanaged_count)
        writer.write_int_value("eligibleButNotAzureAdJoinedCount", self.eligible_but_not_azure_ad_joined_count)
        writer.write_int_value("eligibleCount", self.eligible_count)
        writer.write_int_value("ineligibleCount", self.ineligible_count)
        writer.write_int_value("needsOsUpdateCount", self.needs_os_update_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("scheduledForEnrollmentCount", self.scheduled_for_enrollment_count)
        writer.write_additional_data_value(self.additional_data)
    

