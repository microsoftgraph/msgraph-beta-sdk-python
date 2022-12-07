from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class MacOSFirewallApplication(AdditionalDataHolder, Parsable):
    """
    Represents an app in the list of macOS firewall applications
    """
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
    
    @property
    def allows_incoming_connections(self,) -> Optional[bool]:
        """
        Gets the allowsIncomingConnections property value. Whether or not incoming connections are allowed.
        Returns: Optional[bool]
        """
        return self._allows_incoming_connections
    
    @allows_incoming_connections.setter
    def allows_incoming_connections(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowsIncomingConnections property value. Whether or not incoming connections are allowed.
        Args:
            value: Value to set for the allowsIncomingConnections property.
        """
        self._allows_incoming_connections = value
    
    @property
    def bundle_id(self,) -> Optional[str]:
        """
        Gets the bundleId property value. BundleId of the application.
        Returns: Optional[str]
        """
        return self._bundle_id
    
    @bundle_id.setter
    def bundle_id(self,value: Optional[str] = None) -> None:
        """
        Sets the bundleId property value. BundleId of the application.
        Args:
            value: Value to set for the bundleId property.
        """
        self._bundle_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new macOSFirewallApplication and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Whether or not incoming connections are allowed.
        self._allows_incoming_connections: Optional[bool] = None
        # BundleId of the application.
        self._bundle_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSFirewallApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSFirewallApplication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSFirewallApplication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allows_incoming_connections": lambda n : setattr(self, 'allows_incoming_connections', n.get_bool_value()),
            "bundle_id": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
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
            value: Value to set for the OdataType property.
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
        writer.write_bool_value("allowsIncomingConnections", self.allows_incoming_connections)
        writer.write_str_value("bundleId", self.bundle_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

