from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import business_flow_settings, entity, governance_policy

from . import entity

@dataclass
class BusinessFlow(entity.Entity):
    # The customData property
    custom_data: Optional[str] = None
    # The deDuplicationId property
    de_duplication_id: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policy property
    policy: Optional[governance_policy.GovernancePolicy] = None
    # The policyTemplateId property
    policy_template_id: Optional[str] = None
    # The recordVersion property
    record_version: Optional[str] = None
    # The schemaId property
    schema_id: Optional[str] = None
    # The settings property
    settings: Optional[business_flow_settings.BusinessFlowSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BusinessFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BusinessFlow
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BusinessFlow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import business_flow_settings, entity, governance_policy

        fields: Dict[str, Callable[[Any], None]] = {
            "customData": lambda n : setattr(self, 'custom_data', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deDuplicationId": lambda n : setattr(self, 'de_duplication_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(governance_policy.GovernancePolicy)),
            "policyTemplateId": lambda n : setattr(self, 'policy_template_id', n.get_str_value()),
            "recordVersion": lambda n : setattr(self, 'record_version', n.get_str_value()),
            "schemaId": lambda n : setattr(self, 'schema_id', n.get_str_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(business_flow_settings.BusinessFlowSettings)),
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
        writer.write_str_value("customData", self.custom_data)
        writer.write_str_value("description", self.description)
        writer.write_str_value("deDuplicationId", self.de_duplication_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("policy", self.policy)
        writer.write_str_value("policyTemplateId", self.policy_template_id)
        writer.write_str_value("recordVersion", self.record_version)
        writer.write_str_value("schemaId", self.schema_id)
        writer.write_object_value("settings", self.settings)
    

