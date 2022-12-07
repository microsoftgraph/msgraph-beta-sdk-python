from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

governance_criteria = lazy_import('msgraph.generated.models.governance_criteria')

class RoleMembershipGovernanceCriteria(governance_criteria.GovernanceCriteria):
    def __init__(self,) -> None:
        """
        Instantiates a new RoleMembershipGovernanceCriteria and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.roleMembershipGovernanceCriteria"
        # The roleId property
        self._role_id: Optional[str] = None
        # The roleTemplateId property
        self._role_template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoleMembershipGovernanceCriteria:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RoleMembershipGovernanceCriteria
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RoleMembershipGovernanceCriteria()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "role_id": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "role_template_id": lambda n : setattr(self, 'role_template_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def role_id(self,) -> Optional[str]:
        """
        Gets the roleId property value. The roleId property
        Returns: Optional[str]
        """
        return self._role_id
    
    @role_id.setter
    def role_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleId property value. The roleId property
        Args:
            value: Value to set for the roleId property.
        """
        self._role_id = value
    
    @property
    def role_template_id(self,) -> Optional[str]:
        """
        Gets the roleTemplateId property value. The roleTemplateId property
        Returns: Optional[str]
        """
        return self._role_template_id
    
    @role_template_id.setter
    def role_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleTemplateId property value. The roleTemplateId property
        Args:
            value: Value to set for the roleTemplateId property.
        """
        self._role_template_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("roleId", self.role_id)
        writer.write_str_value("roleTemplateId", self.role_template_id)
    

