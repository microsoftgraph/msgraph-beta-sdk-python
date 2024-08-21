from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.managed_device_remote_action import ManagedDeviceRemoteAction

@dataclass
class ExecuteActionPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The actionName property
    action_name: Optional[ManagedDeviceRemoteAction] = None
    # The carrierUrl property
    carrier_url: Optional[str] = None
    # The deprovisionReason property
    deprovision_reason: Optional[str] = None
    # The deviceIds property
    device_ids: Optional[List[str]] = None
    # The deviceName property
    device_name: Optional[str] = None
    # The keepEnrollmentData property
    keep_enrollment_data: Optional[bool] = None
    # The keepUserData property
    keep_user_data: Optional[bool] = None
    # The notificationBody property
    notification_body: Optional[str] = None
    # The notificationTitle property
    notification_title: Optional[str] = None
    # The organizationalUnitPath property
    organizational_unit_path: Optional[str] = None
    # The persistEsimDataPlan property
    persist_esim_data_plan: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExecuteActionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExecuteActionPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExecuteActionPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models.managed_device_remote_action import ManagedDeviceRemoteAction

        from ....models.managed_device_remote_action import ManagedDeviceRemoteAction

        fields: Dict[str, Callable[[Any], None]] = {
            "actionName": lambda n : setattr(self, 'action_name', n.get_enum_value(ManagedDeviceRemoteAction)),
            "carrierUrl": lambda n : setattr(self, 'carrier_url', n.get_str_value()),
            "deprovisionReason": lambda n : setattr(self, 'deprovision_reason', n.get_str_value()),
            "deviceIds": lambda n : setattr(self, 'device_ids', n.get_collection_of_primitive_values(str)),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "keepEnrollmentData": lambda n : setattr(self, 'keep_enrollment_data', n.get_bool_value()),
            "keepUserData": lambda n : setattr(self, 'keep_user_data', n.get_bool_value()),
            "notificationBody": lambda n : setattr(self, 'notification_body', n.get_str_value()),
            "notificationTitle": lambda n : setattr(self, 'notification_title', n.get_str_value()),
            "organizationalUnitPath": lambda n : setattr(self, 'organizational_unit_path', n.get_str_value()),
            "persistEsimDataPlan": lambda n : setattr(self, 'persist_esim_data_plan', n.get_bool_value()),
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
        writer.write_enum_value("actionName", self.action_name)
        writer.write_str_value("carrierUrl", self.carrier_url)
        writer.write_str_value("deprovisionReason", self.deprovision_reason)
        writer.write_collection_of_primitive_values("deviceIds", self.device_ids)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_bool_value("keepEnrollmentData", self.keep_enrollment_data)
        writer.write_bool_value("keepUserData", self.keep_user_data)
        writer.write_str_value("notificationBody", self.notification_body)
        writer.write_str_value("notificationTitle", self.notification_title)
        writer.write_str_value("organizationalUnitPath", self.organizational_unit_path)
        writer.write_bool_value("persistEsimDataPlan", self.persist_esim_data_plan)
        writer.write_additional_data_value(self.additional_data)
    

