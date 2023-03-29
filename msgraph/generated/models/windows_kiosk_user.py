from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows_kiosk_active_directory_group, windows_kiosk_autologon, windows_kiosk_azure_a_d_group, windows_kiosk_azure_a_d_user, windows_kiosk_local_group, windows_kiosk_local_user, windows_kiosk_visitor

class WindowsKioskUser(AdditionalDataHolder, Parsable):
    """
    The user base class used to identify the account info for the kiosk configuration
    """
    def __init__(self,) -> None:
        """
        Instantiates a new windowsKioskUser and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsKioskUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskUser
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.windowsKioskActiveDirectoryGroup":
                from . import windows_kiosk_active_directory_group

                return windows_kiosk_active_directory_group.WindowsKioskActiveDirectoryGroup()
            if mapping_value == "#microsoft.graph.windowsKioskAutologon":
                from . import windows_kiosk_autologon

                return windows_kiosk_autologon.WindowsKioskAutologon()
            if mapping_value == "#microsoft.graph.windowsKioskAzureADGroup":
                from . import windows_kiosk_azure_a_d_group

                return windows_kiosk_azure_a_d_group.WindowsKioskAzureADGroup()
            if mapping_value == "#microsoft.graph.windowsKioskAzureADUser":
                from . import windows_kiosk_azure_a_d_user

                return windows_kiosk_azure_a_d_user.WindowsKioskAzureADUser()
            if mapping_value == "#microsoft.graph.windowsKioskLocalGroup":
                from . import windows_kiosk_local_group

                return windows_kiosk_local_group.WindowsKioskLocalGroup()
            if mapping_value == "#microsoft.graph.windowsKioskLocalUser":
                from . import windows_kiosk_local_user

                return windows_kiosk_local_user.WindowsKioskLocalUser()
            if mapping_value == "#microsoft.graph.windowsKioskVisitor":
                from . import windows_kiosk_visitor

                return windows_kiosk_visitor.WindowsKioskVisitor()
        return WindowsKioskUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import windows_kiosk_active_directory_group, windows_kiosk_autologon, windows_kiosk_azure_a_d_group, windows_kiosk_azure_a_d_user, windows_kiosk_local_group, windows_kiosk_local_user, windows_kiosk_visitor

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

