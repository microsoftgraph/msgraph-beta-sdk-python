from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
group_policy_category = lazy_import('msgraph.generated.models.group_policy_category')
group_policy_definition_class_type = lazy_import('msgraph.generated.models.group_policy_definition_class_type')
group_policy_definition_file = lazy_import('msgraph.generated.models.group_policy_definition_file')
group_policy_presentation = lazy_import('msgraph.generated.models.group_policy_presentation')
group_policy_type = lazy_import('msgraph.generated.models.group_policy_type')

class GroupPolicyDefinition(entity.Entity):
    @property
    def category(self,) -> Optional[group_policy_category.GroupPolicyCategory]:
        """
        Gets the category property value. The group policy category associated with the definition.
        Returns: Optional[group_policy_category.GroupPolicyCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[group_policy_category.GroupPolicyCategory] = None) -> None:
        """
        Sets the category property value. The group policy category associated with the definition.
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    @property
    def category_path(self,) -> Optional[str]:
        """
        Gets the categoryPath property value. The localized full category path for the policy.
        Returns: Optional[str]
        """
        return self._category_path
    
    @category_path.setter
    def category_path(self,value: Optional[str] = None) -> None:
        """
        Sets the categoryPath property value. The localized full category path for the policy.
        Args:
            value: Value to set for the categoryPath property.
        """
        self._category_path = value
    
    @property
    def class_type(self,) -> Optional[group_policy_definition_class_type.GroupPolicyDefinitionClassType]:
        """
        Gets the classType property value. Group Policy Definition Class Type.
        Returns: Optional[group_policy_definition_class_type.GroupPolicyDefinitionClassType]
        """
        return self._class_type
    
    @class_type.setter
    def class_type(self,value: Optional[group_policy_definition_class_type.GroupPolicyDefinitionClassType] = None) -> None:
        """
        Sets the classType property value. Group Policy Definition Class Type.
        Args:
            value: Value to set for the classType property.
        """
        self._class_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new groupPolicyDefinition and sets the default values.
        """
        super().__init__()
        # The group policy category associated with the definition.
        self._category: Optional[group_policy_category.GroupPolicyCategory] = None
        # The localized full category path for the policy.
        self._category_path: Optional[str] = None
        # Group Policy Definition Class Type.
        self._class_type: Optional[group_policy_definition_class_type.GroupPolicyDefinitionClassType] = None
        # The group policy file associated with the definition.
        self._definition_file: Optional[group_policy_definition_file.GroupPolicyDefinitionFile] = None
        # The localized policy name.
        self._display_name: Optional[str] = None
        # The localized explanation or help text associated with the policy. The default value is empty.
        self._explain_text: Optional[str] = None
        # The category id of the parent category
        self._group_policy_category_id: Optional[Guid] = None
        # Signifies whether or not there are related definitions to this definition
        self._has_related_definitions: Optional[bool] = None
        # The date and time the entity was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # Minimum required CSP version for device configuration in this definition
        self._min_device_csp_version: Optional[str] = None
        # Minimum required CSP version for user configuration in this definition
        self._min_user_csp_version: Optional[str] = None
        # Definition of the next version of this definition
        self._next_version_definition: Optional[GroupPolicyDefinition] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Type of Group Policy File or Definition.
        self._policy_type: Optional[group_policy_type.GroupPolicyType] = None
        # The group policy presentations associated with the definition.
        self._presentations: Optional[List[group_policy_presentation.GroupPolicyPresentation]] = None
        # Definition of the previous version of this definition
        self._previous_version_definition: Optional[GroupPolicyDefinition] = None
        # Localized string used to specify what operating system or application version is affected by the policy.
        self._supported_on: Optional[str] = None
        # Setting definition version
        self._version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyDefinition()
    
    @property
    def definition_file(self,) -> Optional[group_policy_definition_file.GroupPolicyDefinitionFile]:
        """
        Gets the definitionFile property value. The group policy file associated with the definition.
        Returns: Optional[group_policy_definition_file.GroupPolicyDefinitionFile]
        """
        return self._definition_file
    
    @definition_file.setter
    def definition_file(self,value: Optional[group_policy_definition_file.GroupPolicyDefinitionFile] = None) -> None:
        """
        Sets the definitionFile property value. The group policy file associated with the definition.
        Args:
            value: Value to set for the definitionFile property.
        """
        self._definition_file = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The localized policy name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The localized policy name.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def explain_text(self,) -> Optional[str]:
        """
        Gets the explainText property value. The localized explanation or help text associated with the policy. The default value is empty.
        Returns: Optional[str]
        """
        return self._explain_text
    
    @explain_text.setter
    def explain_text(self,value: Optional[str] = None) -> None:
        """
        Sets the explainText property value. The localized explanation or help text associated with the policy. The default value is empty.
        Args:
            value: Value to set for the explainText property.
        """
        self._explain_text = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "category": lambda n : setattr(self, 'category', n.get_object_value(group_policy_category.GroupPolicyCategory)),
            "category_path": lambda n : setattr(self, 'category_path', n.get_str_value()),
            "class_type": lambda n : setattr(self, 'class_type', n.get_enum_value(group_policy_definition_class_type.GroupPolicyDefinitionClassType)),
            "definition_file": lambda n : setattr(self, 'definition_file', n.get_object_value(group_policy_definition_file.GroupPolicyDefinitionFile)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "explain_text": lambda n : setattr(self, 'explain_text', n.get_str_value()),
            "group_policy_category_id": lambda n : setattr(self, 'group_policy_category_id', n.get_object_value(Guid)),
            "has_related_definitions": lambda n : setattr(self, 'has_related_definitions', n.get_bool_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "min_device_csp_version": lambda n : setattr(self, 'min_device_csp_version', n.get_str_value()),
            "min_user_csp_version": lambda n : setattr(self, 'min_user_csp_version', n.get_str_value()),
            "next_version_definition": lambda n : setattr(self, 'next_version_definition', n.get_object_value(GroupPolicyDefinition)),
            "policy_type": lambda n : setattr(self, 'policy_type', n.get_enum_value(group_policy_type.GroupPolicyType)),
            "presentations": lambda n : setattr(self, 'presentations', n.get_collection_of_object_values(group_policy_presentation.GroupPolicyPresentation)),
            "previous_version_definition": lambda n : setattr(self, 'previous_version_definition', n.get_object_value(GroupPolicyDefinition)),
            "supported_on": lambda n : setattr(self, 'supported_on', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_policy_category_id(self,) -> Optional[Guid]:
        """
        Gets the groupPolicyCategoryId property value. The category id of the parent category
        Returns: Optional[Guid]
        """
        return self._group_policy_category_id
    
    @group_policy_category_id.setter
    def group_policy_category_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the groupPolicyCategoryId property value. The category id of the parent category
        Args:
            value: Value to set for the groupPolicyCategoryId property.
        """
        self._group_policy_category_id = value
    
    @property
    def has_related_definitions(self,) -> Optional[bool]:
        """
        Gets the hasRelatedDefinitions property value. Signifies whether or not there are related definitions to this definition
        Returns: Optional[bool]
        """
        return self._has_related_definitions
    
    @has_related_definitions.setter
    def has_related_definitions(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasRelatedDefinitions property value. Signifies whether or not there are related definitions to this definition
        Args:
            value: Value to set for the hasRelatedDefinitions property.
        """
        self._has_related_definitions = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def min_device_csp_version(self,) -> Optional[str]:
        """
        Gets the minDeviceCspVersion property value. Minimum required CSP version for device configuration in this definition
        Returns: Optional[str]
        """
        return self._min_device_csp_version
    
    @min_device_csp_version.setter
    def min_device_csp_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minDeviceCspVersion property value. Minimum required CSP version for device configuration in this definition
        Args:
            value: Value to set for the minDeviceCspVersion property.
        """
        self._min_device_csp_version = value
    
    @property
    def min_user_csp_version(self,) -> Optional[str]:
        """
        Gets the minUserCspVersion property value. Minimum required CSP version for user configuration in this definition
        Returns: Optional[str]
        """
        return self._min_user_csp_version
    
    @min_user_csp_version.setter
    def min_user_csp_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minUserCspVersion property value. Minimum required CSP version for user configuration in this definition
        Args:
            value: Value to set for the minUserCspVersion property.
        """
        self._min_user_csp_version = value
    
    @property
    def next_version_definition(self,) -> Optional[GroupPolicyDefinition]:
        """
        Gets the nextVersionDefinition property value. Definition of the next version of this definition
        Returns: Optional[GroupPolicyDefinition]
        """
        return self._next_version_definition
    
    @next_version_definition.setter
    def next_version_definition(self,value: Optional[GroupPolicyDefinition] = None) -> None:
        """
        Sets the nextVersionDefinition property value. Definition of the next version of this definition
        Args:
            value: Value to set for the nextVersionDefinition property.
        """
        self._next_version_definition = value
    
    @property
    def policy_type(self,) -> Optional[group_policy_type.GroupPolicyType]:
        """
        Gets the policyType property value. Type of Group Policy File or Definition.
        Returns: Optional[group_policy_type.GroupPolicyType]
        """
        return self._policy_type
    
    @policy_type.setter
    def policy_type(self,value: Optional[group_policy_type.GroupPolicyType] = None) -> None:
        """
        Sets the policyType property value. Type of Group Policy File or Definition.
        Args:
            value: Value to set for the policyType property.
        """
        self._policy_type = value
    
    @property
    def presentations(self,) -> Optional[List[group_policy_presentation.GroupPolicyPresentation]]:
        """
        Gets the presentations property value. The group policy presentations associated with the definition.
        Returns: Optional[List[group_policy_presentation.GroupPolicyPresentation]]
        """
        return self._presentations
    
    @presentations.setter
    def presentations(self,value: Optional[List[group_policy_presentation.GroupPolicyPresentation]] = None) -> None:
        """
        Sets the presentations property value. The group policy presentations associated with the definition.
        Args:
            value: Value to set for the presentations property.
        """
        self._presentations = value
    
    @property
    def previous_version_definition(self,) -> Optional[GroupPolicyDefinition]:
        """
        Gets the previousVersionDefinition property value. Definition of the previous version of this definition
        Returns: Optional[GroupPolicyDefinition]
        """
        return self._previous_version_definition
    
    @previous_version_definition.setter
    def previous_version_definition(self,value: Optional[GroupPolicyDefinition] = None) -> None:
        """
        Sets the previousVersionDefinition property value. Definition of the previous version of this definition
        Args:
            value: Value to set for the previousVersionDefinition property.
        """
        self._previous_version_definition = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("category", self.category)
        writer.write_str_value("categoryPath", self.category_path)
        writer.write_enum_value("classType", self.class_type)
        writer.write_object_value("definitionFile", self.definition_file)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("explainText", self.explain_text)
        writer.write_object_value("groupPolicyCategoryId", self.group_policy_category_id)
        writer.write_bool_value("hasRelatedDefinitions", self.has_related_definitions)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("minDeviceCspVersion", self.min_device_csp_version)
        writer.write_str_value("minUserCspVersion", self.min_user_csp_version)
        writer.write_object_value("nextVersionDefinition", self.next_version_definition)
        writer.write_enum_value("policyType", self.policy_type)
        writer.write_collection_of_object_values("presentations", self.presentations)
        writer.write_object_value("previousVersionDefinition", self.previous_version_definition)
        writer.write_str_value("supportedOn", self.supported_on)
        writer.write_str_value("version", self.version)
    
    @property
    def supported_on(self,) -> Optional[str]:
        """
        Gets the supportedOn property value. Localized string used to specify what operating system or application version is affected by the policy.
        Returns: Optional[str]
        """
        return self._supported_on
    
    @supported_on.setter
    def supported_on(self,value: Optional[str] = None) -> None:
        """
        Sets the supportedOn property value. Localized string used to specify what operating system or application version is affected by the policy.
        Args:
            value: Value to set for the supportedOn property.
        """
        self._supported_on = value
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. Setting definition version
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. Setting definition version
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

