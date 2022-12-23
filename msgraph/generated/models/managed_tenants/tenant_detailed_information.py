from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class TenantDetailedInformation(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def city(self,) -> Optional[str]:
        """
        Gets the city property value. The city where the managed tenant is located. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._city
    
    @city.setter
    def city(self,value: Optional[str] = None) -> None:
        """
        Sets the city property value. The city where the managed tenant is located. Optional. Read-only.
        Args:
            value: Value to set for the city property.
        """
        self._city = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new tenantDetailedInformation and sets the default values.
        """
        super().__init__()
        # The city where the managed tenant is located. Optional. Read-only.
        self._city: Optional[str] = None
        # The code for the country where the managed tenant is located. Optional. Read-only.
        self._country_code: Optional[str] = None
        # The name for the country where the managed tenant is located. Optional. Read-only.
        self._country_name: Optional[str] = None
        # The default domain name for the managed tenant. Optional. Read-only.
        self._default_domain_name: Optional[str] = None
        # The display name for the managed tenant.
        self._display_name: Optional[str] = None
        # The business industry associated with the managed tenant. Optional. Read-only.
        self._industry_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The region where the managed tenant is located. Optional. Read-only.
        self._region: Optional[str] = None
        # The business segment associated with the managed tenant. Optional. Read-only.
        self._segment_name: Optional[str] = None
        # The Azure Active Directory tenant identifier for the managed tenant.
        self._tenant_id: Optional[str] = None
        # The vertical associated with the managed tenant. Optional. Read-only.
        self._vertical_name: Optional[str] = None
    
    @property
    def country_code(self,) -> Optional[str]:
        """
        Gets the countryCode property value. The code for the country where the managed tenant is located. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._country_code
    
    @country_code.setter
    def country_code(self,value: Optional[str] = None) -> None:
        """
        Sets the countryCode property value. The code for the country where the managed tenant is located. Optional. Read-only.
        Args:
            value: Value to set for the countryCode property.
        """
        self._country_code = value
    
    @property
    def country_name(self,) -> Optional[str]:
        """
        Gets the countryName property value. The name for the country where the managed tenant is located. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._country_name
    
    @country_name.setter
    def country_name(self,value: Optional[str] = None) -> None:
        """
        Sets the countryName property value. The name for the country where the managed tenant is located. Optional. Read-only.
        Args:
            value: Value to set for the countryName property.
        """
        self._country_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantDetailedInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TenantDetailedInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TenantDetailedInformation()
    
    @property
    def default_domain_name(self,) -> Optional[str]:
        """
        Gets the defaultDomainName property value. The default domain name for the managed tenant. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._default_domain_name
    
    @default_domain_name.setter
    def default_domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultDomainName property value. The default domain name for the managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the defaultDomainName property.
        """
        self._default_domain_name = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the managed tenant.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the managed tenant.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country_code": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "country_name": lambda n : setattr(self, 'country_name', n.get_str_value()),
            "default_domain_name": lambda n : setattr(self, 'default_domain_name', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "industry_name": lambda n : setattr(self, 'industry_name', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
            "segment_name": lambda n : setattr(self, 'segment_name', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "vertical_name": lambda n : setattr(self, 'vertical_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def industry_name(self,) -> Optional[str]:
        """
        Gets the industryName property value. The business industry associated with the managed tenant. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._industry_name
    
    @industry_name.setter
    def industry_name(self,value: Optional[str] = None) -> None:
        """
        Sets the industryName property value. The business industry associated with the managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the industryName property.
        """
        self._industry_name = value
    
    @property
    def region(self,) -> Optional[str]:
        """
        Gets the region property value. The region where the managed tenant is located. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._region
    
    @region.setter
    def region(self,value: Optional[str] = None) -> None:
        """
        Sets the region property value. The region where the managed tenant is located. Optional. Read-only.
        Args:
            value: Value to set for the region property.
        """
        self._region = value
    
    @property
    def segment_name(self,) -> Optional[str]:
        """
        Gets the segmentName property value. The business segment associated with the managed tenant. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._segment_name
    
    @segment_name.setter
    def segment_name(self,value: Optional[str] = None) -> None:
        """
        Sets the segmentName property value. The business segment associated with the managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the segmentName property.
        """
        self._segment_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("city", self.city)
        writer.write_str_value("countryCode", self.country_code)
        writer.write_str_value("countryName", self.country_name)
        writer.write_str_value("defaultDomainName", self.default_domain_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("industryName", self.industry_name)
        writer.write_str_value("region", self.region)
        writer.write_str_value("segmentName", self.segment_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("verticalName", self.vertical_name)
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    
    @property
    def vertical_name(self,) -> Optional[str]:
        """
        Gets the verticalName property value. The vertical associated with the managed tenant. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._vertical_name
    
    @vertical_name.setter
    def vertical_name(self,value: Optional[str] = None) -> None:
        """
        Sets the verticalName property value. The vertical associated with the managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the verticalName property.
        """
        self._vertical_name = value
    

