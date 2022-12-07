from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
group_policy_configuration_type = lazy_import('msgraph.generated.models.group_policy_configuration_type')
group_policy_definition = lazy_import('msgraph.generated.models.group_policy_definition')
group_policy_presentation_value = lazy_import('msgraph.generated.models.group_policy_presentation_value')

class GroupPolicyDefinitionValue(entity.Entity):
    """
    The definition value entity stores the value for a single group policy definition.
    """
    @property
    def configuration_type(self,) -> Optional[group_policy_configuration_type.GroupPolicyConfigurationType]:
        """
        Gets the configurationType property value. Group Policy Configuration Type
        Returns: Optional[group_policy_configuration_type.GroupPolicyConfigurationType]
        """
        return self._configuration_type
    
    @configuration_type.setter
    def configuration_type(self,value: Optional[group_policy_configuration_type.GroupPolicyConfigurationType] = None) -> None:
        """
        Sets the configurationType property value. Group Policy Configuration Type
        Args:
            value: Value to set for the configurationType property.
        """
        self._configuration_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new groupPolicyDefinitionValue and sets the default values.
        """
        super().__init__()
        # Group Policy Configuration Type
        self._configuration_type: Optional[group_policy_configuration_type.GroupPolicyConfigurationType] = None
        # The date and time the object was created.
        self._created_date_time: Optional[datetime] = None
        # The associated group policy definition with the value.
        self._definition: Optional[group_policy_definition.GroupPolicyDefinition] = None
        # Enables or disables the associated group policy definition.
        self._enabled: Optional[bool] = None
        # The date and time the entity was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The associated group policy presentation values with the definition value.
        self._presentation_values: Optional[List[group_policy_presentation_value.GroupPolicyPresentationValue]] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the object was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the object was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyDefinitionValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyDefinitionValue
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyDefinitionValue()
    
    @property
    def definition(self,) -> Optional[group_policy_definition.GroupPolicyDefinition]:
        """
        Gets the definition property value. The associated group policy definition with the value.
        Returns: Optional[group_policy_definition.GroupPolicyDefinition]
        """
        return self._definition
    
    @definition.setter
    def definition(self,value: Optional[group_policy_definition.GroupPolicyDefinition] = None) -> None:
        """
        Sets the definition property value. The associated group policy definition with the value.
        Args:
            value: Value to set for the definition property.
        """
        self._definition = value
    
    @property
    def enabled(self,) -> Optional[bool]:
        """
        Gets the enabled property value. Enables or disables the associated group policy definition.
        Returns: Optional[bool]
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the enabled property value. Enables or disables the associated group policy definition.
        Args:
            value: Value to set for the enabled property.
        """
        self._enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "configuration_type": lambda n : setattr(self, 'configuration_type', n.get_enum_value(group_policy_configuration_type.GroupPolicyConfigurationType)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "definition": lambda n : setattr(self, 'definition', n.get_object_value(group_policy_definition.GroupPolicyDefinition)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "presentation_values": lambda n : setattr(self, 'presentation_values', n.get_collection_of_object_values(group_policy_presentation_value.GroupPolicyPresentationValue)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    def presentation_values(self,) -> Optional[List[group_policy_presentation_value.GroupPolicyPresentationValue]]:
        """
        Gets the presentationValues property value. The associated group policy presentation values with the definition value.
        Returns: Optional[List[group_policy_presentation_value.GroupPolicyPresentationValue]]
        """
        return self._presentation_values
    
    @presentation_values.setter
    def presentation_values(self,value: Optional[List[group_policy_presentation_value.GroupPolicyPresentationValue]] = None) -> None:
        """
        Sets the presentationValues property value. The associated group policy presentation values with the definition value.
        Args:
            value: Value to set for the presentationValues property.
        """
        self._presentation_values = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("configurationType", self.configuration_type)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("definition", self.definition)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("presentationValues", self.presentation_values)
    

