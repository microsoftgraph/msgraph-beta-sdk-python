from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ServicePrincipalCreationConditionSet(entity.Entity):
    """
    Casts the previous resource to application.
    """
    @property
    def application_ids(self,) -> Optional[List[str]]:
        """
        Gets the applicationIds property value. The applicationIds property
        Returns: Optional[List[str]]
        """
        return self._application_ids
    
    @application_ids.setter
    def application_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the applicationIds property value. The applicationIds property
        Args:
            value: Value to set for the applicationIds property.
        """
        self._application_ids = value
    
    @property
    def application_publisher_ids(self,) -> Optional[List[str]]:
        """
        Gets the applicationPublisherIds property value. The applicationPublisherIds property
        Returns: Optional[List[str]]
        """
        return self._application_publisher_ids
    
    @application_publisher_ids.setter
    def application_publisher_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the applicationPublisherIds property value. The applicationPublisherIds property
        Args:
            value: Value to set for the applicationPublisherIds property.
        """
        self._application_publisher_ids = value
    
    @property
    def applications_from_verified_publisher_only(self,) -> Optional[bool]:
        """
        Gets the applicationsFromVerifiedPublisherOnly property value. The applicationsFromVerifiedPublisherOnly property
        Returns: Optional[bool]
        """
        return self._applications_from_verified_publisher_only
    
    @applications_from_verified_publisher_only.setter
    def applications_from_verified_publisher_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationsFromVerifiedPublisherOnly property value. The applicationsFromVerifiedPublisherOnly property
        Args:
            value: Value to set for the applicationsFromVerifiedPublisherOnly property.
        """
        self._applications_from_verified_publisher_only = value
    
    @property
    def application_tenant_ids(self,) -> Optional[List[str]]:
        """
        Gets the applicationTenantIds property value. The applicationTenantIds property
        Returns: Optional[List[str]]
        """
        return self._application_tenant_ids
    
    @application_tenant_ids.setter
    def application_tenant_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the applicationTenantIds property value. The applicationTenantIds property
        Args:
            value: Value to set for the applicationTenantIds property.
        """
        self._application_tenant_ids = value
    
    @property
    def certified_applications_only(self,) -> Optional[bool]:
        """
        Gets the certifiedApplicationsOnly property value. The certifiedApplicationsOnly property
        Returns: Optional[bool]
        """
        return self._certified_applications_only
    
    @certified_applications_only.setter
    def certified_applications_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the certifiedApplicationsOnly property value. The certifiedApplicationsOnly property
        Args:
            value: Value to set for the certifiedApplicationsOnly property.
        """
        self._certified_applications_only = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new servicePrincipalCreationConditionSet and sets the default values.
        """
        super().__init__()
        # The applicationIds property
        self._application_ids: Optional[List[str]] = None
        # The applicationPublisherIds property
        self._application_publisher_ids: Optional[List[str]] = None
        # The applicationsFromVerifiedPublisherOnly property
        self._applications_from_verified_publisher_only: Optional[bool] = None
        # The applicationTenantIds property
        self._application_tenant_ids: Optional[List[str]] = None
        # The certifiedApplicationsOnly property
        self._certified_applications_only: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServicePrincipalCreationConditionSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipalCreationConditionSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServicePrincipalCreationConditionSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_ids": lambda n : setattr(self, 'application_ids', n.get_collection_of_primitive_values(str)),
            "application_publisher_ids": lambda n : setattr(self, 'application_publisher_ids', n.get_collection_of_primitive_values(str)),
            "applications_from_verified_publisher_only": lambda n : setattr(self, 'applications_from_verified_publisher_only', n.get_bool_value()),
            "application_tenant_ids": lambda n : setattr(self, 'application_tenant_ids', n.get_collection_of_primitive_values(str)),
            "certified_applications_only": lambda n : setattr(self, 'certified_applications_only', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("applicationIds", self.application_ids)
        writer.write_collection_of_primitive_values("applicationPublisherIds", self.application_publisher_ids)
        writer.write_bool_value("applicationsFromVerifiedPublisherOnly", self.applications_from_verified_publisher_only)
        writer.write_collection_of_primitive_values("applicationTenantIds", self.application_tenant_ids)
        writer.write_bool_value("certifiedApplicationsOnly", self.certified_applications_only)
    

