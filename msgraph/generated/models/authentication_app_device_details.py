from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AuthenticationAppDeviceDetails(AdditionalDataHolder, Parsable):
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
    def app_version(self,) -> Optional[str]:
        """
        Gets the appVersion property value. The version of the client authentication app used during the authentication step.
        Returns: Optional[str]
        """
        return self._app_version
    
    @app_version.setter
    def app_version(self,value: Optional[str] = None) -> None:
        """
        Sets the appVersion property value. The version of the client authentication app used during the authentication step.
        Args:
            value: Value to set for the appVersion property.
        """
        self._app_version = value
    
    @property
    def client_app(self,) -> Optional[str]:
        """
        Gets the clientApp property value. The name of the client authentication app used during the authentication step.
        Returns: Optional[str]
        """
        return self._client_app
    
    @client_app.setter
    def client_app(self,value: Optional[str] = None) -> None:
        """
        Sets the clientApp property value. The name of the client authentication app used during the authentication step.
        Args:
            value: Value to set for the clientApp property.
        """
        self._client_app = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new authenticationAppDeviceDetails and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The version of the client authentication app used during the authentication step.
        self._app_version: Optional[str] = None
        # The name of the client authentication app used during the authentication step.
        self._client_app: Optional[str] = None
        # ID of the device used during the authentication step.
        self._device_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The operating system running on the device used for the authentication step.
        self._operating_system: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationAppDeviceDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationAppDeviceDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationAppDeviceDetails()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. ID of the device used during the authentication step.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. ID of the device used during the authentication step.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_version": lambda n : setattr(self, 'app_version', n.get_str_value()),
            "client_app": lambda n : setattr(self, 'client_app', n.get_str_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operating_system": lambda n : setattr(self, 'operating_system', n.get_str_value()),
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
    def operating_system(self,) -> Optional[str]:
        """
        Gets the operatingSystem property value. The operating system running on the device used for the authentication step.
        Returns: Optional[str]
        """
        return self._operating_system
    
    @operating_system.setter
    def operating_system(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystem property value. The operating system running on the device used for the authentication step.
        Args:
            value: Value to set for the operatingSystem property.
        """
        self._operating_system = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("appVersion", self.app_version)
        writer.write_str_value("clientApp", self.client_app)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_additional_data_value(self.additional_data)
    

