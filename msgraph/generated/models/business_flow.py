from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

business_flow_settings = lazy_import('msgraph.generated.models.business_flow_settings')
entity = lazy_import('msgraph.generated.models.entity')
governance_policy = lazy_import('msgraph.generated.models.governance_policy')

class BusinessFlow(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new businessFlow and sets the default values.
        """
        super().__init__()
        # The customData property
        self._custom_data: Optional[str] = None
        # The deDuplicationId property
        self._de_duplication_id: Optional[str] = None
        # The description property
        self._description: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The policy property
        self._policy: Optional[governance_policy.GovernancePolicy] = None
        # The policyTemplateId property
        self._policy_template_id: Optional[str] = None
        # The recordVersion property
        self._record_version: Optional[str] = None
        # The schemaId property
        self._schema_id: Optional[str] = None
        # The settings property
        self._settings: Optional[business_flow_settings.BusinessFlowSettings] = None
    
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
    
    @property
    def custom_data(self,) -> Optional[str]:
        """
        Gets the customData property value. The customData property
        Returns: Optional[str]
        """
        return self._custom_data
    
    @custom_data.setter
    def custom_data(self,value: Optional[str] = None) -> None:
        """
        Sets the customData property value. The customData property
        Args:
            value: Value to set for the customData property.
        """
        self._custom_data = value
    
    @property
    def de_duplication_id(self,) -> Optional[str]:
        """
        Gets the deDuplicationId property value. The deDuplicationId property
        Returns: Optional[str]
        """
        return self._de_duplication_id
    
    @de_duplication_id.setter
    def de_duplication_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deDuplicationId property value. The deDuplicationId property
        Args:
            value: Value to set for the deDuplicationId property.
        """
        self._de_duplication_id = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
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
            "custom_data": lambda n : setattr(self, 'custom_data', n.get_str_value()),
            "de_duplication_id": lambda n : setattr(self, 'de_duplication_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(governance_policy.GovernancePolicy)),
            "policy_template_id": lambda n : setattr(self, 'policy_template_id', n.get_str_value()),
            "record_version": lambda n : setattr(self, 'record_version', n.get_str_value()),
            "schema_id": lambda n : setattr(self, 'schema_id', n.get_str_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(business_flow_settings.BusinessFlowSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def policy(self,) -> Optional[governance_policy.GovernancePolicy]:
        """
        Gets the policy property value. The policy property
        Returns: Optional[governance_policy.GovernancePolicy]
        """
        return self._policy
    
    @policy.setter
    def policy(self,value: Optional[governance_policy.GovernancePolicy] = None) -> None:
        """
        Sets the policy property value. The policy property
        Args:
            value: Value to set for the policy property.
        """
        self._policy = value
    
    @property
    def policy_template_id(self,) -> Optional[str]:
        """
        Gets the policyTemplateId property value. The policyTemplateId property
        Returns: Optional[str]
        """
        return self._policy_template_id
    
    @policy_template_id.setter
    def policy_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the policyTemplateId property value. The policyTemplateId property
        Args:
            value: Value to set for the policyTemplateId property.
        """
        self._policy_template_id = value
    
    @property
    def record_version(self,) -> Optional[str]:
        """
        Gets the recordVersion property value. The recordVersion property
        Returns: Optional[str]
        """
        return self._record_version
    
    @record_version.setter
    def record_version(self,value: Optional[str] = None) -> None:
        """
        Sets the recordVersion property value. The recordVersion property
        Args:
            value: Value to set for the recordVersion property.
        """
        self._record_version = value
    
    @property
    def schema_id(self,) -> Optional[str]:
        """
        Gets the schemaId property value. The schemaId property
        Returns: Optional[str]
        """
        return self._schema_id
    
    @schema_id.setter
    def schema_id(self,value: Optional[str] = None) -> None:
        """
        Sets the schemaId property value. The schemaId property
        Args:
            value: Value to set for the schemaId property.
        """
        self._schema_id = value
    
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
        writer.write_str_value("deDuplicationId", self.de_duplication_id)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("policy", self.policy)
        writer.write_str_value("policyTemplateId", self.policy_template_id)
        writer.write_str_value("recordVersion", self.record_version)
        writer.write_str_value("schemaId", self.schema_id)
        writer.write_object_value("settings", self.settings)
    
    @property
    def settings(self,) -> Optional[business_flow_settings.BusinessFlowSettings]:
        """
        Gets the settings property value. The settings property
        Returns: Optional[business_flow_settings.BusinessFlowSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[business_flow_settings.BusinessFlowSettings] = None) -> None:
        """
        Sets the settings property value. The settings property
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    

