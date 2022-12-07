from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TenantInformation(AdditionalDataHolder, Parsable):
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
        Instantiates a new tenantInformation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Primary domain name of an Azure AD tenant.
        self._default_domain_name: Optional[str] = None
        # Display name of an Azure AD tenant.
        self._display_name: Optional[str] = None
        # Name shown to users that sign in to an Azure AD tenant.
        self._federation_brand_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Unique identifier of an Azure AD tenant.
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TenantInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TenantInformation()
    
    @property
    def default_domain_name(self,) -> Optional[str]:
        """
        Gets the defaultDomainName property value. Primary domain name of an Azure AD tenant.
        Returns: Optional[str]
        """
        return self._default_domain_name
    
    @default_domain_name.setter
    def default_domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultDomainName property value. Primary domain name of an Azure AD tenant.
        Args:
            value: Value to set for the defaultDomainName property.
        """
        self._default_domain_name = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of an Azure AD tenant.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of an Azure AD tenant.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def federation_brand_name(self,) -> Optional[str]:
        """
        Gets the federationBrandName property value. Name shown to users that sign in to an Azure AD tenant.
        Returns: Optional[str]
        """
        return self._federation_brand_name
    
    @federation_brand_name.setter
    def federation_brand_name(self,value: Optional[str] = None) -> None:
        """
        Sets the federationBrandName property value. Name shown to users that sign in to an Azure AD tenant.
        Args:
            value: Value to set for the federationBrandName property.
        """
        self._federation_brand_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_domain_name": lambda n : setattr(self, 'default_domain_name', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "federation_brand_name": lambda n : setattr(self, 'federation_brand_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_str_value("defaultDomainName", self.default_domain_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("federationBrandName", self.federation_brand_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. Unique identifier of an Azure AD tenant.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. Unique identifier of an Azure AD tenant.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    

