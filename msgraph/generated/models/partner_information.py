from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import partner_tenant_type

class PartnerInformation(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new partnerInformation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The commerceUrl property
        self._commerce_url: Optional[str] = None
        # The companyName property
        self._company_name: Optional[str] = None
        # The companyType property
        self._company_type: Optional[partner_tenant_type.PartnerTenantType] = None
        # The helpUrl property
        self._help_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The partnerTenantId property
        self._partner_tenant_id: Optional[str] = None
        # The supportEmails property
        self._support_emails: Optional[List[str]] = None
        # The supportTelephones property
        self._support_telephones: Optional[List[str]] = None
        # The supportUrl property
        self._support_url: Optional[str] = None
    
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
    def commerce_url(self,) -> Optional[str]:
        """
        Gets the commerceUrl property value. The commerceUrl property
        Returns: Optional[str]
        """
        return self._commerce_url
    
    @commerce_url.setter
    def commerce_url(self,value: Optional[str] = None) -> None:
        """
        Sets the commerceUrl property value. The commerceUrl property
        Args:
            value: Value to set for the commerce_url property.
        """
        self._commerce_url = value
    
    @property
    def company_name(self,) -> Optional[str]:
        """
        Gets the companyName property value. The companyName property
        Returns: Optional[str]
        """
        return self._company_name
    
    @company_name.setter
    def company_name(self,value: Optional[str] = None) -> None:
        """
        Sets the companyName property value. The companyName property
        Args:
            value: Value to set for the company_name property.
        """
        self._company_name = value
    
    @property
    def company_type(self,) -> Optional[partner_tenant_type.PartnerTenantType]:
        """
        Gets the companyType property value. The companyType property
        Returns: Optional[partner_tenant_type.PartnerTenantType]
        """
        return self._company_type
    
    @company_type.setter
    def company_type(self,value: Optional[partner_tenant_type.PartnerTenantType] = None) -> None:
        """
        Sets the companyType property value. The companyType property
        Args:
            value: Value to set for the company_type property.
        """
        self._company_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PartnerInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PartnerInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PartnerInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import partner_tenant_type

        fields: Dict[str, Callable[[Any], None]] = {
            "commerceUrl": lambda n : setattr(self, 'commerce_url', n.get_str_value()),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "companyType": lambda n : setattr(self, 'company_type', n.get_enum_value(partner_tenant_type.PartnerTenantType)),
            "helpUrl": lambda n : setattr(self, 'help_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "partnerTenantId": lambda n : setattr(self, 'partner_tenant_id', n.get_str_value()),
            "supportEmails": lambda n : setattr(self, 'support_emails', n.get_collection_of_primitive_values(str)),
            "supportTelephones": lambda n : setattr(self, 'support_telephones', n.get_collection_of_primitive_values(str)),
            "supportUrl": lambda n : setattr(self, 'support_url', n.get_str_value()),
        }
        return fields
    
    @property
    def help_url(self,) -> Optional[str]:
        """
        Gets the helpUrl property value. The helpUrl property
        Returns: Optional[str]
        """
        return self._help_url
    
    @help_url.setter
    def help_url(self,value: Optional[str] = None) -> None:
        """
        Sets the helpUrl property value. The helpUrl property
        Args:
            value: Value to set for the help_url property.
        """
        self._help_url = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def partner_tenant_id(self,) -> Optional[str]:
        """
        Gets the partnerTenantId property value. The partnerTenantId property
        Returns: Optional[str]
        """
        return self._partner_tenant_id
    
    @partner_tenant_id.setter
    def partner_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the partnerTenantId property value. The partnerTenantId property
        Args:
            value: Value to set for the partner_tenant_id property.
        """
        self._partner_tenant_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("commerceUrl", self.commerce_url)
        writer.write_str_value("companyName", self.company_name)
        writer.write_enum_value("companyType", self.company_type)
        writer.write_str_value("helpUrl", self.help_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("partnerTenantId", self.partner_tenant_id)
        writer.write_collection_of_primitive_values("supportEmails", self.support_emails)
        writer.write_collection_of_primitive_values("supportTelephones", self.support_telephones)
        writer.write_str_value("supportUrl", self.support_url)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def support_emails(self,) -> Optional[List[str]]:
        """
        Gets the supportEmails property value. The supportEmails property
        Returns: Optional[List[str]]
        """
        return self._support_emails
    
    @support_emails.setter
    def support_emails(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the supportEmails property value. The supportEmails property
        Args:
            value: Value to set for the support_emails property.
        """
        self._support_emails = value
    
    @property
    def support_telephones(self,) -> Optional[List[str]]:
        """
        Gets the supportTelephones property value. The supportTelephones property
        Returns: Optional[List[str]]
        """
        return self._support_telephones
    
    @support_telephones.setter
    def support_telephones(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the supportTelephones property value. The supportTelephones property
        Args:
            value: Value to set for the support_telephones property.
        """
        self._support_telephones = value
    
    @property
    def support_url(self,) -> Optional[str]:
        """
        Gets the supportUrl property value. The supportUrl property
        Returns: Optional[str]
        """
        return self._support_url
    
    @support_url.setter
    def support_url(self,value: Optional[str] = None) -> None:
        """
        Sets the supportUrl property value. The supportUrl property
        Args:
            value: Value to set for the support_url property.
        """
        self._support_url = value
    

