from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AirPrintDestination(AdditionalDataHolder, Parsable):
    """
    Represents an AirPrint destination.
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
        Instantiates a new airPrintDestination and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # If true AirPrint connections are secured by Transport Layer Security (TLS). Default is false. Available in iOS 11.0 and later.
        self._force_tls: Optional[bool] = None
        # The IP Address of the AirPrint destination.
        self._ip_address: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The listening port of the AirPrint destination. If this key is not specified AirPrint will use the default port. Available in iOS 11.0 and later.
        self._port: Optional[int] = None
        # The Resource Path associated with the printer. This corresponds to the rp parameter of the ipps.tcp Bonjour record. For example: printers/Canon_MG5300_series, printers/Xerox_Phaser_7600, ipp/print, Epson_IPP_Printer.
        self._resource_path: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AirPrintDestination:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AirPrintDestination
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AirPrintDestination()
    
    @property
    def force_tls(self,) -> Optional[bool]:
        """
        Gets the forceTls property value. If true AirPrint connections are secured by Transport Layer Security (TLS). Default is false. Available in iOS 11.0 and later.
        Returns: Optional[bool]
        """
        return self._force_tls
    
    @force_tls.setter
    def force_tls(self,value: Optional[bool] = None) -> None:
        """
        Sets the forceTls property value. If true AirPrint connections are secured by Transport Layer Security (TLS). Default is false. Available in iOS 11.0 and later.
        Args:
            value: Value to set for the forceTls property.
        """
        self._force_tls = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "force_tls": lambda n : setattr(self, 'force_tls', n.get_bool_value()),
            "ip_address": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "resource_path": lambda n : setattr(self, 'resource_path', n.get_str_value()),
        }
        return fields
    
    @property
    def ip_address(self,) -> Optional[str]:
        """
        Gets the ipAddress property value. The IP Address of the AirPrint destination.
        Returns: Optional[str]
        """
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddress property value. The IP Address of the AirPrint destination.
        Args:
            value: Value to set for the ipAddress property.
        """
        self._ip_address = value
    
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
    def port(self,) -> Optional[int]:
        """
        Gets the port property value. The listening port of the AirPrint destination. If this key is not specified AirPrint will use the default port. Available in iOS 11.0 and later.
        Returns: Optional[int]
        """
        return self._port
    
    @port.setter
    def port(self,value: Optional[int] = None) -> None:
        """
        Sets the port property value. The listening port of the AirPrint destination. If this key is not specified AirPrint will use the default port. Available in iOS 11.0 and later.
        Args:
            value: Value to set for the port property.
        """
        self._port = value
    
    @property
    def resource_path(self,) -> Optional[str]:
        """
        Gets the resourcePath property value. The Resource Path associated with the printer. This corresponds to the rp parameter of the ipps.tcp Bonjour record. For example: printers/Canon_MG5300_series, printers/Xerox_Phaser_7600, ipp/print, Epson_IPP_Printer.
        Returns: Optional[str]
        """
        return self._resource_path
    
    @resource_path.setter
    def resource_path(self,value: Optional[str] = None) -> None:
        """
        Sets the resourcePath property value. The Resource Path associated with the printer. This corresponds to the rp parameter of the ipps.tcp Bonjour record. For example: printers/Canon_MG5300_series, printers/Xerox_Phaser_7600, ipp/print, Epson_IPP_Printer.
        Args:
            value: Value to set for the resourcePath property.
        """
        self._resource_path = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("forceTls", self.force_tls)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("port", self.port)
        writer.write_str_value("resourcePath", self.resource_path)
        writer.write_additional_data_value(self.additional_data)
    

