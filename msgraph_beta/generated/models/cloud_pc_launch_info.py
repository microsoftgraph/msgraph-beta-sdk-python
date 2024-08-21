from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CloudPcLaunchInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The unique identifier of the Cloud PC.
    cloud_pc_id: Optional[str] = None
    # The connect URL of the Cloud PC.
    cloud_pc_launch_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the Cloud PC supports switch functionality. If the value is true, it supports switch functionality; otherwise,  false.
    windows365_switch_compatible: Optional[bool] = None
    # Indicates the reason the Cloud PC doesn't support switch. CPCOsVersionNotMeetRequirement indicates that the user needs to update their Cloud PC operation system version. CPCHardwareNotMeetRequirement indicates that the Cloud PC needs more CPU or RAM to support the functionality.
    windows365_switch_not_compatible_reason: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcLaunchInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcLaunchInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcLaunchInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "cloudPcId": lambda n : setattr(self, 'cloud_pc_id', n.get_str_value()),
            "cloudPcLaunchUrl": lambda n : setattr(self, 'cloud_pc_launch_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "windows365SwitchCompatible": lambda n : setattr(self, 'windows365_switch_compatible', n.get_bool_value()),
            "windows365SwitchNotCompatibleReason": lambda n : setattr(self, 'windows365_switch_not_compatible_reason', n.get_str_value()),
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
        writer.write_str_value("cloudPcId", self.cloud_pc_id)
        writer.write_str_value("cloudPcLaunchUrl", self.cloud_pc_launch_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("windows365SwitchCompatible", self.windows365_switch_compatible)
        writer.write_str_value("windows365SwitchNotCompatibleReason", self.windows365_switch_not_compatible_reason)
        writer.write_additional_data_value(self.additional_data)
    

