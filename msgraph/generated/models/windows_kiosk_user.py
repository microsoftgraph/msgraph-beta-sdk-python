from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows_kiosk_active_directory_group, windows_kiosk_autologon, windows_kiosk_azure_a_d_group, windows_kiosk_azure_a_d_user, windows_kiosk_local_group, windows_kiosk_local_user, windows_kiosk_visitor

@dataclass
class WindowsKioskUser(AdditionalDataHolder, Parsable):
    """
    The user base class used to identify the account info for the kiosk configuration
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskUser
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskActiveDirectoryGroup".casefold():
            from . import windows_kiosk_active_directory_group

            return windows_kiosk_active_directory_group.WindowsKioskActiveDirectoryGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskAutologon".casefold():
            from . import windows_kiosk_autologon

            return windows_kiosk_autologon.WindowsKioskAutologon()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskAzureADGroup".casefold():
            from . import windows_kiosk_azure_a_d_group

            return windows_kiosk_azure_a_d_group.WindowsKioskAzureADGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskAzureADUser".casefold():
            from . import windows_kiosk_azure_a_d_user

            return windows_kiosk_azure_a_d_user.WindowsKioskAzureADUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskLocalGroup".casefold():
            from . import windows_kiosk_local_group

            return windows_kiosk_local_group.WindowsKioskLocalGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskLocalUser".casefold():
            from . import windows_kiosk_local_user

            return windows_kiosk_local_user.WindowsKioskLocalUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskVisitor".casefold():
            from . import windows_kiosk_visitor

            return windows_kiosk_visitor.WindowsKioskVisitor()
        return WindowsKioskUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import windows_kiosk_active_directory_group, windows_kiosk_autologon, windows_kiosk_azure_a_d_group, windows_kiosk_azure_a_d_user, windows_kiosk_local_group, windows_kiosk_local_user, windows_kiosk_visitor

        from . import windows_kiosk_active_directory_group, windows_kiosk_autologon, windows_kiosk_azure_a_d_group, windows_kiosk_azure_a_d_user, windows_kiosk_local_group, windows_kiosk_local_user, windows_kiosk_visitor

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

