from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ContinuousAccessEvaluationPolicy(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new ContinuousAccessEvaluationPolicy and sets the default values.
        """
        super().__init__()
        # Continuous access evaluation automatically blocks access to resources and applications in near real time when a user's access is removed or a client IP address changes. Read-only.
        self._description: Optional[str] = None
        # The value is always Continuous Access Evaluation. Read-only.
        self._display_name: Optional[str] = None
        # The collection of group identifiers in scope for evaluation. All groups are in scope when the collection is empty. Read-only.
        self._groups: Optional[List[str]] = None
        # true to indicate whether continuous access evaluation should be performed; otherwise false. Read-only.
        self._is_enabled: Optional[bool] = None
        # true to indicate that the continuous access evaluation policy settings should be or has been migrated to the conditional access policy.
        self._migrate: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The collection of user identifiers in scope for evaluation. All users are in scope when the collection is empty. Read-only.
        self._users: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContinuousAccessEvaluationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ContinuousAccessEvaluationPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ContinuousAccessEvaluationPolicy()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Continuous access evaluation automatically blocks access to resources and applications in near real time when a user's access is removed or a client IP address changes. Read-only.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Continuous access evaluation automatically blocks access to resources and applications in near real time when a user's access is removed or a client IP address changes. Read-only.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The value is always Continuous Access Evaluation. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The value is always Continuous Access Evaluation. Read-only.
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
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_primitive_values(str)),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "migrate": lambda n : setattr(self, 'migrate', n.get_bool_value()),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def groups(self,) -> Optional[List[str]]:
        """
        Gets the groups property value. The collection of group identifiers in scope for evaluation. All groups are in scope when the collection is empty. Read-only.
        Returns: Optional[List[str]]
        """
        return self._groups
    
    @groups.setter
    def groups(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the groups property value. The collection of group identifiers in scope for evaluation. All groups are in scope when the collection is empty. Read-only.
        Args:
            value: Value to set for the groups property.
        """
        self._groups = value
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. true to indicate whether continuous access evaluation should be performed; otherwise false. Read-only.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. true to indicate whether continuous access evaluation should be performed; otherwise false. Read-only.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
    @property
    def migrate(self,) -> Optional[bool]:
        """
        Gets the migrate property value. true to indicate that the continuous access evaluation policy settings should be or has been migrated to the conditional access policy.
        Returns: Optional[bool]
        """
        return self._migrate
    
    @migrate.setter
    def migrate(self,value: Optional[bool] = None) -> None:
        """
        Sets the migrate property value. true to indicate that the continuous access evaluation policy settings should be or has been migrated to the conditional access policy.
        Args:
            value: Value to set for the migrate property.
        """
        self._migrate = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("groups", self.groups)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_bool_value("migrate", self.migrate)
        writer.write_collection_of_primitive_values("users", self.users)
    
    @property
    def users(self,) -> Optional[List[str]]:
        """
        Gets the users property value. The collection of user identifiers in scope for evaluation. All users are in scope when the collection is empty. Read-only.
        Returns: Optional[List[str]]
        """
        return self._users
    
    @users.setter
    def users(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the users property value. The collection of user identifiers in scope for evaluation. All users are in scope when the collection is empty. Read-only.
        Args:
            value: Value to set for the users property.
        """
        self._users = value
    

