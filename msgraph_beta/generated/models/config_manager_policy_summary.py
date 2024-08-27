from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ConfigManagerPolicySummary(AdditionalDataHolder, BackedModel, Parsable):
    """
    A ConfigManager policy summary.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The number of devices evaluated to be compliant by the policy.
    compliant_device_count: Optional[int] = None
    # The number of devices that have have been remediated by the policy.
    enforced_device_count: Optional[int] = None
    # The number of devices that failed to be evaluated by the policy.
    failed_device_count: Optional[int] = None
    # The number of devices evaluated to be noncompliant by the policy.
    non_compliant_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of devices that have acknowledged the policy but are pending evaluation.
    pending_device_count: Optional[int] = None
    # The number of devices targeted by the policy.
    targeted_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConfigManagerPolicySummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfigManagerPolicySummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConfigManagerPolicySummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "compliantDeviceCount": lambda n : setattr(self, 'compliant_device_count', n.get_int_value()),
            "enforcedDeviceCount": lambda n : setattr(self, 'enforced_device_count', n.get_int_value()),
            "failedDeviceCount": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
            "nonCompliantDeviceCount": lambda n : setattr(self, 'non_compliant_device_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pendingDeviceCount": lambda n : setattr(self, 'pending_device_count', n.get_int_value()),
            "targetedDeviceCount": lambda n : setattr(self, 'targeted_device_count', n.get_int_value()),
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
        writer.write_int_value("compliantDeviceCount", self.compliant_device_count)
        writer.write_int_value("enforcedDeviceCount", self.enforced_device_count)
        writer.write_int_value("failedDeviceCount", self.failed_device_count)
        writer.write_int_value("nonCompliantDeviceCount", self.non_compliant_device_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("pendingDeviceCount", self.pending_device_count)
        writer.write_int_value("targetedDeviceCount", self.targeted_device_count)
        writer.write_additional_data_value(self.additional_data)
    

