from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ConfigurationManagerClientInformation(AdditionalDataHolder, Parsable):
    """
    Configuration Manager client information synced from SCCM
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
    def client_identifier(self,) -> Optional[str]:
        """
        Gets the clientIdentifier property value. Configuration Manager Client Id from SCCM
        Returns: Optional[str]
        """
        return self._client_identifier
    
    @client_identifier.setter
    def client_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the clientIdentifier property value. Configuration Manager Client Id from SCCM
        Args:
            value: Value to set for the clientIdentifier property.
        """
        self._client_identifier = value
    
    @property
    def client_version(self,) -> Optional[str]:
        """
        Gets the clientVersion property value. Configuration Manager Client version from SCCM
        Returns: Optional[str]
        """
        return self._client_version
    
    @client_version.setter
    def client_version(self,value: Optional[str] = None) -> None:
        """
        Sets the clientVersion property value. Configuration Manager Client version from SCCM
        Args:
            value: Value to set for the clientVersion property.
        """
        self._client_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new configurationManagerClientInformation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Configuration Manager Client Id from SCCM
        self._client_identifier: Optional[str] = None
        # Configuration Manager Client version from SCCM
        self._client_version: Optional[str] = None
        # Configuration Manager Client blocked status from SCCM
        self._is_blocked: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConfigurationManagerClientInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationManagerClientInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConfigurationManagerClientInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "client_identifier": lambda n : setattr(self, 'client_identifier', n.get_str_value()),
            "client_version": lambda n : setattr(self, 'client_version', n.get_str_value()),
            "is_blocked": lambda n : setattr(self, 'is_blocked', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_blocked(self,) -> Optional[bool]:
        """
        Gets the isBlocked property value. Configuration Manager Client blocked status from SCCM
        Returns: Optional[bool]
        """
        return self._is_blocked
    
    @is_blocked.setter
    def is_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the isBlocked property value. Configuration Manager Client blocked status from SCCM
        Args:
            value: Value to set for the isBlocked property.
        """
        self._is_blocked = value
    
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
        writer.write_str_value("clientIdentifier", self.client_identifier)
        writer.write_str_value("clientVersion", self.client_version)
        writer.write_bool_value("isBlocked", self.is_blocked)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

