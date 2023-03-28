from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import tenant_contact_information
    from .. import entity

from .. import entity

class TenantCustomizedInformation(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new tenantCustomizedInformation and sets the default values.
        """
        super().__init__()
        # The collection of contacts for the managed tenant. Optional.
        self._contacts: Optional[List[tenant_contact_information.TenantContactInformation]] = None
        # The display name for the managed tenant. Required. Read-only.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The Azure Active Directory tenant identifier for the managed tenant. Optional. Read-only.
        self._tenant_id: Optional[str] = None
        # The website for the managed tenant. Required.
        self._website: Optional[str] = None
    
    @property
    def contacts(self,) -> Optional[List[tenant_contact_information.TenantContactInformation]]:
        """
        Gets the contacts property value. The collection of contacts for the managed tenant. Optional.
        Returns: Optional[List[tenant_contact_information.TenantContactInformation]]
        """
        return self._contacts
    
    @contacts.setter
    def contacts(self,value: Optional[List[tenant_contact_information.TenantContactInformation]] = None) -> None:
        """
        Sets the contacts property value. The collection of contacts for the managed tenant. Optional.
        Args:
            value: Value to set for the contacts property.
        """
        self._contacts = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantCustomizedInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TenantCustomizedInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TenantCustomizedInformation()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the managed tenant. Required. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the managed tenant. Required. Read-only.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import tenant_contact_information
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "contacts": lambda n : setattr(self, 'contacts', n.get_collection_of_object_values(tenant_contact_information.TenantContactInformation)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "website": lambda n : setattr(self, 'website', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("contacts", self.contacts)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("website", self.website)
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    
    @property
    def website(self,) -> Optional[str]:
        """
        Gets the website property value. The website for the managed tenant. Required.
        Returns: Optional[str]
        """
        return self._website
    
    @website.setter
    def website(self,value: Optional[str] = None) -> None:
        """
        Sets the website property value. The website for the managed tenant. Required.
        Args:
            value: Value to set for the website property.
        """
        self._website = value
    

