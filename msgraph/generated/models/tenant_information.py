from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TenantInformation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Primary domain name of an Azure AD tenant.
    default_domain_name: Optional[str] = None
    # Display name of an Azure AD tenant.
    display_name: Optional[str] = None
    # Name shown to users that sign in to an Azure AD tenant.
    federation_brand_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unique identifier of an Azure AD tenant.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantInformation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TenantInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "defaultDomainName": lambda n : setattr(self, 'default_domain_name', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "federationBrandName": lambda n : setattr(self, 'federation_brand_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("defaultDomainName", self.default_domain_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("federationBrandName", self.federation_brand_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_additional_data_value(self.additional_data)
    

