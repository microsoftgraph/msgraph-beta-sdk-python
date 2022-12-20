from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_resource = lazy_import('msgraph.generated.models.access_package_resource')
entity = lazy_import('msgraph.generated.models.entity')

class AccessPackageResourceRole(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def access_package_resource(self,) -> Optional[access_package_resource.AccessPackageResource]:
        """
        Gets the accessPackageResource property value. The accessPackageResource property
        Returns: Optional[access_package_resource.AccessPackageResource]
        """
        return self._access_package_resource
    
    @access_package_resource.setter
    def access_package_resource(self,value: Optional[access_package_resource.AccessPackageResource] = None) -> None:
        """
        Sets the accessPackageResource property value. The accessPackageResource property
        Args:
            value: Value to set for the accessPackageResource property.
        """
        self._access_package_resource = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageResourceRole and sets the default values.
        """
        super().__init__()
        # The accessPackageResource property
        self._access_package_resource: Optional[access_package_resource.AccessPackageResource] = None
        # A description for the resource role.
        self._description: Optional[str] = None
        # The display name of the resource role such as the role defined by the application.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The unique identifier of the resource role in the origin system. For a SharePoint Online site, the originId will be the sequence number of the role in the site.
        self._origin_id: Optional[str] = None
        # The type of the resource in the origin system, such as SharePointOnline, AadApplication or AadGroup.
        self._origin_system: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageResourceRole:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceRole
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageResourceRole()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. A description for the resource role.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. A description for the resource role.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the resource role such as the role defined by the application.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the resource role such as the role defined by the application.
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
            "access_package_resource": lambda n : setattr(self, 'access_package_resource', n.get_object_value(access_package_resource.AccessPackageResource)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "origin_id": lambda n : setattr(self, 'origin_id', n.get_str_value()),
            "origin_system": lambda n : setattr(self, 'origin_system', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def origin_id(self,) -> Optional[str]:
        """
        Gets the originId property value. The unique identifier of the resource role in the origin system. For a SharePoint Online site, the originId will be the sequence number of the role in the site.
        Returns: Optional[str]
        """
        return self._origin_id
    
    @origin_id.setter
    def origin_id(self,value: Optional[str] = None) -> None:
        """
        Sets the originId property value. The unique identifier of the resource role in the origin system. For a SharePoint Online site, the originId will be the sequence number of the role in the site.
        Args:
            value: Value to set for the originId property.
        """
        self._origin_id = value
    
    @property
    def origin_system(self,) -> Optional[str]:
        """
        Gets the originSystem property value. The type of the resource in the origin system, such as SharePointOnline, AadApplication or AadGroup.
        Returns: Optional[str]
        """
        return self._origin_system
    
    @origin_system.setter
    def origin_system(self,value: Optional[str] = None) -> None:
        """
        Sets the originSystem property value. The type of the resource in the origin system, such as SharePointOnline, AadApplication or AadGroup.
        Args:
            value: Value to set for the originSystem property.
        """
        self._origin_system = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("accessPackageResource", self.access_package_resource)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("originId", self.origin_id)
        writer.write_str_value("originSystem", self.origin_system)
    

