from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mac_o_s_device_local_admin_account_detail import MacOSDeviceLocalAdminAccountDetail

@dataclass
class DeviceLocalAdminAccountDetail(AdditionalDataHolder, BackedModel, Parsable):
    """
    Base class for properties related to configured and Intune-managed local administrator account
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The last rotation date and time of the local admin account password. Read-only.
    password_last_rotation_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceLocalAdminAccountDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceLocalAdminAccountDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSDeviceLocalAdminAccountDetail".casefold():
            from .mac_o_s_device_local_admin_account_detail import MacOSDeviceLocalAdminAccountDetail

            return MacOSDeviceLocalAdminAccountDetail()
        return DeviceLocalAdminAccountDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mac_o_s_device_local_admin_account_detail import MacOSDeviceLocalAdminAccountDetail

        from .mac_o_s_device_local_admin_account_detail import MacOSDeviceLocalAdminAccountDetail

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "passwordLastRotationDateTime": lambda n : setattr(self, 'password_last_rotation_date_time', n.get_datetime_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("passwordLastRotationDateTime", self.password_last_rotation_date_time)
        writer.write_additional_data_value(self.additional_data)
    

