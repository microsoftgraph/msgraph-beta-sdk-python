from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ProviderTenantSetting(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def azure_tenant_id(self,) -> Optional[str]:
        """
        Gets the azureTenantId property value. The azureTenantId property
        Returns: Optional[str]
        """
        return self._azure_tenant_id
    
    @azure_tenant_id.setter
    def azure_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureTenantId property value. The azureTenantId property
        Args:
            value: Value to set for the azureTenantId property.
        """
        self._azure_tenant_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new providerTenantSetting and sets the default values.
        """
        super().__init__()
        # The azureTenantId property
        self._azure_tenant_id: Optional[str] = None
        # The enabled property
        self._enabled: Optional[bool] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The provider property
        self._provider: Optional[str] = None
        # The vendor property
        self._vendor: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProviderTenantSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProviderTenantSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProviderTenantSetting()
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "azure_tenant_id": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_str_value()),
            "vendor": lambda n : setattr(self, 'vendor', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("provider", self.provider)
        writer.write_str_value("vendor", self.vendor)
    
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
    

