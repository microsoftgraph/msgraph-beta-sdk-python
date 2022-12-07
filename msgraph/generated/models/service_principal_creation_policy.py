from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

policy_base = lazy_import('msgraph.generated.models.policy_base')
service_principal_creation_condition_set = lazy_import('msgraph.generated.models.service_principal_creation_condition_set')

class ServicePrincipalCreationPolicy(policy_base.PolicyBase):
    def __init__(self,) -> None:
        """
        Instantiates a new ServicePrincipalCreationPolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.servicePrincipalCreationPolicy"
        # The excludes property
        self._excludes: Optional[List[service_principal_creation_condition_set.ServicePrincipalCreationConditionSet]] = None
        # The includes property
        self._includes: Optional[List[service_principal_creation_condition_set.ServicePrincipalCreationConditionSet]] = None
        # The isBuiltIn property
        self._is_built_in: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServicePrincipalCreationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipalCreationPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServicePrincipalCreationPolicy()
    
    @property
    def excludes(self,) -> Optional[List[service_principal_creation_condition_set.ServicePrincipalCreationConditionSet]]:
        """
        Gets the excludes property value. The excludes property
        Returns: Optional[List[service_principal_creation_condition_set.ServicePrincipalCreationConditionSet]]
        """
        return self._excludes
    
    @excludes.setter
    def excludes(self,value: Optional[List[service_principal_creation_condition_set.ServicePrincipalCreationConditionSet]] = None) -> None:
        """
        Sets the excludes property value. The excludes property
        Args:
            value: Value to set for the excludes property.
        """
        self._excludes = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "excludes": lambda n : setattr(self, 'excludes', n.get_collection_of_object_values(service_principal_creation_condition_set.ServicePrincipalCreationConditionSet)),
            "includes": lambda n : setattr(self, 'includes', n.get_collection_of_object_values(service_principal_creation_condition_set.ServicePrincipalCreationConditionSet)),
            "is_built_in": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def includes(self,) -> Optional[List[service_principal_creation_condition_set.ServicePrincipalCreationConditionSet]]:
        """
        Gets the includes property value. The includes property
        Returns: Optional[List[service_principal_creation_condition_set.ServicePrincipalCreationConditionSet]]
        """
        return self._includes
    
    @includes.setter
    def includes(self,value: Optional[List[service_principal_creation_condition_set.ServicePrincipalCreationConditionSet]] = None) -> None:
        """
        Sets the includes property value. The includes property
        Args:
            value: Value to set for the includes property.
        """
        self._includes = value
    
    @property
    def is_built_in(self,) -> Optional[bool]:
        """
        Gets the isBuiltIn property value. The isBuiltIn property
        Returns: Optional[bool]
        """
        return self._is_built_in
    
    @is_built_in.setter
    def is_built_in(self,value: Optional[bool] = None) -> None:
        """
        Sets the isBuiltIn property value. The isBuiltIn property
        Args:
            value: Value to set for the isBuiltIn property.
        """
        self._is_built_in = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("excludes", self.excludes)
        writer.write_collection_of_object_values("includes", self.includes)
        writer.write_bool_value("isBuiltIn", self.is_built_in)
    

