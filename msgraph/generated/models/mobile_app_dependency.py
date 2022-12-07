from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app_dependency_type = lazy_import('msgraph.generated.models.mobile_app_dependency_type')
mobile_app_relationship = lazy_import('msgraph.generated.models.mobile_app_relationship')

class MobileAppDependency(mobile_app_relationship.MobileAppRelationship):
    def __init__(self,) -> None:
        """
        Instantiates a new MobileAppDependency and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.mobileAppDependency"
        # Indicates the dependency type associated with a relationship between two mobile apps.
        self._dependency_type: Optional[mobile_app_dependency_type.MobileAppDependencyType] = None
        # The total number of apps that directly or indirectly depend on the parent app.
        self._dependent_app_count: Optional[int] = None
        # The total number of apps the child app directly or indirectly depends on.
        self._depends_on_app_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppDependency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppDependency
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppDependency()
    
    @property
    def dependency_type(self,) -> Optional[mobile_app_dependency_type.MobileAppDependencyType]:
        """
        Gets the dependencyType property value. Indicates the dependency type associated with a relationship between two mobile apps.
        Returns: Optional[mobile_app_dependency_type.MobileAppDependencyType]
        """
        return self._dependency_type
    
    @dependency_type.setter
    def dependency_type(self,value: Optional[mobile_app_dependency_type.MobileAppDependencyType] = None) -> None:
        """
        Sets the dependencyType property value. Indicates the dependency type associated with a relationship between two mobile apps.
        Args:
            value: Value to set for the dependencyType property.
        """
        self._dependency_type = value
    
    @property
    def dependent_app_count(self,) -> Optional[int]:
        """
        Gets the dependentAppCount property value. The total number of apps that directly or indirectly depend on the parent app.
        Returns: Optional[int]
        """
        return self._dependent_app_count
    
    @dependent_app_count.setter
    def dependent_app_count(self,value: Optional[int] = None) -> None:
        """
        Sets the dependentAppCount property value. The total number of apps that directly or indirectly depend on the parent app.
        Args:
            value: Value to set for the dependentAppCount property.
        """
        self._dependent_app_count = value
    
    @property
    def depends_on_app_count(self,) -> Optional[int]:
        """
        Gets the dependsOnAppCount property value. The total number of apps the child app directly or indirectly depends on.
        Returns: Optional[int]
        """
        return self._depends_on_app_count
    
    @depends_on_app_count.setter
    def depends_on_app_count(self,value: Optional[int] = None) -> None:
        """
        Sets the dependsOnAppCount property value. The total number of apps the child app directly or indirectly depends on.
        Args:
            value: Value to set for the dependsOnAppCount property.
        """
        self._depends_on_app_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "dependency_type": lambda n : setattr(self, 'dependency_type', n.get_enum_value(mobile_app_dependency_type.MobileAppDependencyType)),
            "dependent_app_count": lambda n : setattr(self, 'dependent_app_count', n.get_int_value()),
            "depends_on_app_count": lambda n : setattr(self, 'depends_on_app_count', n.get_int_value()),
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
        writer.write_enum_value("dependencyType", self.dependency_type)
        writer.write_int_value("dependentAppCount", self.dependent_app_count)
        writer.write_int_value("dependsOnAppCount", self.depends_on_app_count)
    

