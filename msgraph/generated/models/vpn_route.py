from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class VpnRoute(AdditionalDataHolder, Parsable):
    """
    VPN Route definition.
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new vpnRoute and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Destination prefix (IPv4/v6 address).
        self._destination_prefix: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Prefix size. (1-32). Valid values 1 to 32
        self._prefix_size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VpnRoute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VpnRoute
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VpnRoute()
    
    @property
    def destination_prefix(self,) -> Optional[str]:
        """
        Gets the destinationPrefix property value. Destination prefix (IPv4/v6 address).
        Returns: Optional[str]
        """
        return self._destination_prefix
    
    @destination_prefix.setter
    def destination_prefix(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationPrefix property value. Destination prefix (IPv4/v6 address).
        Args:
            value: Value to set for the destinationPrefix property.
        """
        self._destination_prefix = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "destination_prefix": lambda n : setattr(self, 'destination_prefix', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "prefix_size": lambda n : setattr(self, 'prefix_size', n.get_int_value()),
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
    
    @property
    def prefix_size(self,) -> Optional[int]:
        """
        Gets the prefixSize property value. Prefix size. (1-32). Valid values 1 to 32
        Returns: Optional[int]
        """
        return self._prefix_size
    
    @prefix_size.setter
    def prefix_size(self,value: Optional[int] = None) -> None:
        """
        Sets the prefixSize property value. Prefix size. (1-32). Valid values 1 to 32
        Args:
            value: Value to set for the prefixSize property.
        """
        self._prefix_size = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("destinationPrefix", self.destination_prefix)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("prefixSize", self.prefix_size)
        writer.write_additional_data_value(self.additional_data)
    

