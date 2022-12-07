from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class SecurityProviderStatus(AdditionalDataHolder, Parsable):
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
        Instantiates a new securityProviderStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The enabled property
        self._enabled: Optional[bool] = None
        # The endpoint property
        self._endpoint: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The provider property
        self._provider: Optional[str] = None
        # The region property
        self._region: Optional[str] = None
        # The vendor property
        self._vendor: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecurityProviderStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecurityProviderStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecurityProviderStatus()
    
    @property
    def enabled(self,) -> Optional[bool]:
        """
        Gets the enabled property value. The enabled property
        Returns: Optional[bool]
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the enabled property value. The enabled property
        Args:
            value: Value to set for the enabled property.
        """
        self._enabled = value
    
    @property
    def endpoint(self,) -> Optional[str]:
        """
        Gets the endpoint property value. The endpoint property
        Returns: Optional[str]
        """
        return self._endpoint
    
    @endpoint.setter
    def endpoint(self,value: Optional[str] = None) -> None:
        """
        Sets the endpoint property value. The endpoint property
        Args:
            value: Value to set for the endpoint property.
        """
        self._endpoint = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "endpoint": lambda n : setattr(self, 'endpoint', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
            "vendor": lambda n : setattr(self, 'vendor', n.get_str_value()),
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
    def provider(self,) -> Optional[str]:
        """
        Gets the provider property value. The provider property
        Returns: Optional[str]
        """
        return self._provider
    
    @provider.setter
    def provider(self,value: Optional[str] = None) -> None:
        """
        Sets the provider property value. The provider property
        Args:
            value: Value to set for the provider property.
        """
        self._provider = value
    
    @property
    def region(self,) -> Optional[str]:
        """
        Gets the region property value. The region property
        Returns: Optional[str]
        """
        return self._region
    
    @region.setter
    def region(self,value: Optional[str] = None) -> None:
        """
        Sets the region property value. The region property
        Args:
            value: Value to set for the region property.
        """
        self._region = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("endpoint", self.endpoint)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("provider", self.provider)
        writer.write_str_value("region", self.region)
        writer.write_str_value("vendor", self.vendor)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def vendor(self,) -> Optional[str]:
        """
        Gets the vendor property value. The vendor property
        Returns: Optional[str]
        """
        return self._vendor
    
    @vendor.setter
    def vendor(self,value: Optional[str] = None) -> None:
        """
        Sets the vendor property value. The vendor property
        Args:
            value: Value to set for the vendor property.
        """
        self._vendor = value
    

