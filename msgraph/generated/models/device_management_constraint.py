from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_enum_constraint, device_management_intent_setting_secret_constraint, device_management_setting_abstract_implementation_constraint, device_management_setting_app_constraint, device_management_setting_boolean_constraint, device_management_setting_collection_constraint, device_management_setting_enrollment_type_constraint, device_management_setting_file_constraint, device_management_setting_integer_constraint, device_management_setting_profile_constraint, device_management_setting_regex_constraint, device_management_setting_required_constraint, device_management_setting_sddl_constraint, device_management_setting_string_length_constraint, device_management_setting_xml_constraint

@dataclass
class DeviceManagementConstraint(AdditionalDataHolder, Parsable):
    """
    Base entity for a constraint
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConstraint
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementEnumConstraint".casefold():
            from . import device_management_enum_constraint

            return device_management_enum_constraint.DeviceManagementEnumConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementIntentSettingSecretConstraint".casefold():
            from . import device_management_intent_setting_secret_constraint

            return device_management_intent_setting_secret_constraint.DeviceManagementIntentSettingSecretConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingAbstractImplementationConstraint".casefold():
            from . import device_management_setting_abstract_implementation_constraint

            return device_management_setting_abstract_implementation_constraint.DeviceManagementSettingAbstractImplementationConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingAppConstraint".casefold():
            from . import device_management_setting_app_constraint

            return device_management_setting_app_constraint.DeviceManagementSettingAppConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingBooleanConstraint".casefold():
            from . import device_management_setting_boolean_constraint

            return device_management_setting_boolean_constraint.DeviceManagementSettingBooleanConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingCollectionConstraint".casefold():
            from . import device_management_setting_collection_constraint

            return device_management_setting_collection_constraint.DeviceManagementSettingCollectionConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingEnrollmentTypeConstraint".casefold():
            from . import device_management_setting_enrollment_type_constraint

            return device_management_setting_enrollment_type_constraint.DeviceManagementSettingEnrollmentTypeConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingFileConstraint".casefold():
            from . import device_management_setting_file_constraint

            return device_management_setting_file_constraint.DeviceManagementSettingFileConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingIntegerConstraint".casefold():
            from . import device_management_setting_integer_constraint

            return device_management_setting_integer_constraint.DeviceManagementSettingIntegerConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingProfileConstraint".casefold():
            from . import device_management_setting_profile_constraint

            return device_management_setting_profile_constraint.DeviceManagementSettingProfileConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingRegexConstraint".casefold():
            from . import device_management_setting_regex_constraint

            return device_management_setting_regex_constraint.DeviceManagementSettingRegexConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingRequiredConstraint".casefold():
            from . import device_management_setting_required_constraint

            return device_management_setting_required_constraint.DeviceManagementSettingRequiredConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingSddlConstraint".casefold():
            from . import device_management_setting_sddl_constraint

            return device_management_setting_sddl_constraint.DeviceManagementSettingSddlConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingStringLengthConstraint".casefold():
            from . import device_management_setting_string_length_constraint

            return device_management_setting_string_length_constraint.DeviceManagementSettingStringLengthConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingXmlConstraint".casefold():
            from . import device_management_setting_xml_constraint

            return device_management_setting_xml_constraint.DeviceManagementSettingXmlConstraint()
        return DeviceManagementConstraint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_enum_constraint, device_management_intent_setting_secret_constraint, device_management_setting_abstract_implementation_constraint, device_management_setting_app_constraint, device_management_setting_boolean_constraint, device_management_setting_collection_constraint, device_management_setting_enrollment_type_constraint, device_management_setting_file_constraint, device_management_setting_integer_constraint, device_management_setting_profile_constraint, device_management_setting_regex_constraint, device_management_setting_required_constraint, device_management_setting_sddl_constraint, device_management_setting_string_length_constraint, device_management_setting_xml_constraint

        from . import device_management_enum_constraint, device_management_intent_setting_secret_constraint, device_management_setting_abstract_implementation_constraint, device_management_setting_app_constraint, device_management_setting_boolean_constraint, device_management_setting_collection_constraint, device_management_setting_enrollment_type_constraint, device_management_setting_file_constraint, device_management_setting_integer_constraint, device_management_setting_profile_constraint, device_management_setting_regex_constraint, device_management_setting_required_constraint, device_management_setting_sddl_constraint, device_management_setting_string_length_constraint, device_management_setting_xml_constraint

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

