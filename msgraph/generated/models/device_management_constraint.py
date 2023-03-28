from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_enum_constraint, device_management_intent_setting_secret_constraint, device_management_setting_abstract_implementation_constraint, device_management_setting_app_constraint, device_management_setting_boolean_constraint, device_management_setting_collection_constraint, device_management_setting_enrollment_type_constraint, device_management_setting_file_constraint, device_management_setting_integer_constraint, device_management_setting_profile_constraint, device_management_setting_regex_constraint, device_management_setting_required_constraint, device_management_setting_sddl_constraint, device_management_setting_string_length_constraint, device_management_setting_xml_constraint

class DeviceManagementConstraint(AdditionalDataHolder, Parsable):
    """
    Base entity for a constraint
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConstraint and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConstraint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.deviceManagementEnumConstraint":
                from . import device_management_enum_constraint

                return device_management_enum_constraint.DeviceManagementEnumConstraint()
            if mapping_value == "#microsoft.graph.deviceManagementIntentSettingSecretConstraint":
                from . import device_management_intent_setting_secret_constraint

                return device_management_intent_setting_secret_constraint.DeviceManagementIntentSettingSecretConstraint()
            if mapping_value == "#microsoft.graph.deviceManagementSettingAbstractImplementationConstraint":
                from . import device_management_setting_abstract_implementation_constraint

                return device_management_setting_abstract_implementation_constraint.DeviceManagementSettingAbstractImplementationConstraint()
            if mapping_value == "#microsoft.graph.deviceManagementSettingAppConstraint":
                from . import device_management_setting_app_constraint

                return device_management_setting_app_constraint.DeviceManagementSettingAppConstraint()
            if mapping_value == "#microsoft.graph.deviceManagementSettingBooleanConstraint":
                from . import device_management_setting_boolean_constraint

                return device_management_setting_boolean_constraint.DeviceManagementSettingBooleanConstraint()
            if mapping_value == "#microsoft.graph.deviceManagementSettingCollectionConstraint":
                from . import device_management_setting_collection_constraint

                return device_management_setting_collection_constraint.DeviceManagementSettingCollectionConstraint()
            if mapping_value == "#microsoft.graph.deviceManagementSettingEnrollmentTypeConstraint":
                from . import device_management_setting_enrollment_type_constraint

                return device_management_setting_enrollment_type_constraint.DeviceManagementSettingEnrollmentTypeConstraint()
            if mapping_value == "#microsoft.graph.deviceManagementSettingFileConstraint":
                from . import device_management_setting_file_constraint

                return device_management_setting_file_constraint.DeviceManagementSettingFileConstraint()
            if mapping_value == "#microsoft.graph.deviceManagementSettingIntegerConstraint":
                from . import device_management_setting_integer_constraint

                return device_management_setting_integer_constraint.DeviceManagementSettingIntegerConstraint()
            if mapping_value == "#microsoft.graph.deviceManagementSettingProfileConstraint":
                from . import device_management_setting_profile_constraint

                return device_management_setting_profile_constraint.DeviceManagementSettingProfileConstraint()
            if mapping_value == "#microsoft.graph.deviceManagementSettingRegexConstraint":
                from . import device_management_setting_regex_constraint

                return device_management_setting_regex_constraint.DeviceManagementSettingRegexConstraint()
            if mapping_value == "#microsoft.graph.deviceManagementSettingRequiredConstraint":
                from . import device_management_setting_required_constraint

                return device_management_setting_required_constraint.DeviceManagementSettingRequiredConstraint()
            if mapping_value == "#microsoft.graph.deviceManagementSettingSddlConstraint":
                from . import device_management_setting_sddl_constraint

                return device_management_setting_sddl_constraint.DeviceManagementSettingSddlConstraint()
            if mapping_value == "#microsoft.graph.deviceManagementSettingStringLengthConstraint":
                from . import device_management_setting_string_length_constraint

                return device_management_setting_string_length_constraint.DeviceManagementSettingStringLengthConstraint()
            if mapping_value == "#microsoft.graph.deviceManagementSettingXmlConstraint":
                from . import device_management_setting_xml_constraint

                return device_management_setting_xml_constraint.DeviceManagementSettingXmlConstraint()
        return DeviceManagementConstraint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_enum_constraint, device_management_intent_setting_secret_constraint, device_management_setting_abstract_implementation_constraint, device_management_setting_app_constraint, device_management_setting_boolean_constraint, device_management_setting_collection_constraint, device_management_setting_enrollment_type_constraint, device_management_setting_file_constraint, device_management_setting_integer_constraint, device_management_setting_profile_constraint, device_management_setting_regex_constraint, device_management_setting_required_constraint, device_management_setting_sddl_constraint, device_management_setting_string_length_constraint, device_management_setting_xml_constraint

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

