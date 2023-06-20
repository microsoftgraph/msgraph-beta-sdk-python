from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import workload_onboarding_status

@dataclass
class WorkloadStatus(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The display name for the workload. Required. Read-only.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time the workload was offboarded. Optional. Read-only.
    offboarded_date_time: Optional[datetime] = None
    # The date and time the workload was onboarded. Optional. Read-only.
    onboarded_date_time: Optional[datetime] = None
    # The onboardingStatus property
    onboarding_status: Optional[workload_onboarding_status.WorkloadOnboardingStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkloadStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkloadStatus
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkloadStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import workload_onboarding_status

        from . import workload_onboarding_status

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offboardedDateTime": lambda n : setattr(self, 'offboarded_date_time', n.get_datetime_value()),
            "onboardedDateTime": lambda n : setattr(self, 'onboarded_date_time', n.get_datetime_value()),
            "onboardingStatus": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(workload_onboarding_status.WorkloadOnboardingStatus)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("offboardedDateTime", self.offboarded_date_time)
        writer.write_datetime_value("onboardedDateTime", self.onboarded_date_time)
        writer.write_enum_value("onboardingStatus", self.onboarding_status)
        writer.write_additional_data_value(self.additional_data)
    

