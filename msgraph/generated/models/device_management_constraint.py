from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_enum_constraint import DeviceManagementEnumConstraint
    from .device_management_intent_setting_secret_constraint import DeviceManagementIntentSettingSecretConstraint
    from .device_management_setting_abstract_implementation_constraint import DeviceManagementSettingAbstractImplementationConstraint
    from .device_management_setting_app_constraint import DeviceManagementSettingAppConstraint
    from .device_management_setting_boolean_constraint import DeviceManagementSettingBooleanConstraint
    from .device_management_setting_collection_constraint import DeviceManagementSettingCollectionConstraint
    from .device_management_setting_enrollment_type_constraint import DeviceManagementSettingEnrollmentTypeConstraint
    from .device_management_setting_file_constraint import DeviceManagementSettingFileConstraint
    from .device_management_setting_integer_constraint import DeviceManagementSettingIntegerConstraint
    from .device_management_setting_profile_constraint import DeviceManagementSettingProfileConstraint
    from .device_management_setting_regex_constraint import DeviceManagementSettingRegexConstraint
    from .device_management_setting_required_constraint import DeviceManagementSettingRequiredConstraint
    from .device_management_setting_sddl_constraint import DeviceManagementSettingSddlConstraint
    from .device_management_setting_string_length_constraint import DeviceManagementSettingStringLengthConstraint
    from .device_management_setting_xml_constraint import DeviceManagementSettingXmlConstraint

@dataclass
class DeviceManagementConstraint(AdditionalDataHolder, BackedModel, Parsable):
    """
    Base entity for a constraint
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConstraint
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementEnumConstraint".casefold():
            from .device_management_enum_constraint import DeviceManagementEnumConstraint

            return DeviceManagementEnumConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementIntentSettingSecretConstraint".casefold():
            from .device_management_intent_setting_secret_constraint import DeviceManagementIntentSettingSecretConstraint

            return DeviceManagementIntentSettingSecretConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingAbstractImplementationConstraint".casefold():
            from .device_management_setting_abstract_implementation_constraint import DeviceManagementSettingAbstractImplementationConstraint

            return DeviceManagementSettingAbstractImplementationConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingAppConstraint".casefold():
            from .device_management_setting_app_constraint import DeviceManagementSettingAppConstraint

            return DeviceManagementSettingAppConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingBooleanConstraint".casefold():
            from .device_management_setting_boolean_constraint import DeviceManagementSettingBooleanConstraint

            return DeviceManagementSettingBooleanConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingCollectionConstraint".casefold():
            from .device_management_setting_collection_constraint import DeviceManagementSettingCollectionConstraint

            return DeviceManagementSettingCollectionConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingEnrollmentTypeConstraint".casefold():
            from .device_management_setting_enrollment_type_constraint import DeviceManagementSettingEnrollmentTypeConstraint

            return DeviceManagementSettingEnrollmentTypeConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingFileConstraint".casefold():
            from .device_management_setting_file_constraint import DeviceManagementSettingFileConstraint

            return DeviceManagementSettingFileConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingIntegerConstraint".casefold():
            from .device_management_setting_integer_constraint import DeviceManagementSettingIntegerConstraint

            return DeviceManagementSettingIntegerConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingProfileConstraint".casefold():
            from .device_management_setting_profile_constraint import DeviceManagementSettingProfileConstraint

            return DeviceManagementSettingProfileConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingRegexConstraint".casefold():
            from .device_management_setting_regex_constraint import DeviceManagementSettingRegexConstraint

            return DeviceManagementSettingRegexConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingRequiredConstraint".casefold():
            from .device_management_setting_required_constraint import DeviceManagementSettingRequiredConstraint

            return DeviceManagementSettingRequiredConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingSddlConstraint".casefold():
            from .device_management_setting_sddl_constraint import DeviceManagementSettingSddlConstraint

            return DeviceManagementSettingSddlConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingStringLengthConstraint".casefold():
            from .device_management_setting_string_length_constraint import DeviceManagementSettingStringLengthConstraint

            return DeviceManagementSettingStringLengthConstraint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementSettingXmlConstraint".casefold():
            from .device_management_setting_xml_constraint import DeviceManagementSettingXmlConstraint

            return DeviceManagementSettingXmlConstraint()
        return DeviceManagementConstraint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_enum_constraint import DeviceManagementEnumConstraint
        from .device_management_intent_setting_secret_constraint import DeviceManagementIntentSettingSecretConstraint
        from .device_management_setting_abstract_implementation_constraint import DeviceManagementSettingAbstractImplementationConstraint
        from .device_management_setting_app_constraint import DeviceManagementSettingAppConstraint
        from .device_management_setting_boolean_constraint import DeviceManagementSettingBooleanConstraint
        from .device_management_setting_collection_constraint import DeviceManagementSettingCollectionConstraint
        from .device_management_setting_enrollment_type_constraint import DeviceManagementSettingEnrollmentTypeConstraint
        from .device_management_setting_file_constraint import DeviceManagementSettingFileConstraint
        from .device_management_setting_integer_constraint import DeviceManagementSettingIntegerConstraint
        from .device_management_setting_profile_constraint import DeviceManagementSettingProfileConstraint
        from .device_management_setting_regex_constraint import DeviceManagementSettingRegexConstraint
        from .device_management_setting_required_constraint import DeviceManagementSettingRequiredConstraint
        from .device_management_setting_sddl_constraint import DeviceManagementSettingSddlConstraint
        from .device_management_setting_string_length_constraint import DeviceManagementSettingStringLengthConstraint
        from .device_management_setting_xml_constraint import DeviceManagementSettingXmlConstraint

        from .device_management_enum_constraint import DeviceManagementEnumConstraint
        from .device_management_intent_setting_secret_constraint import DeviceManagementIntentSettingSecretConstraint
        from .device_management_setting_abstract_implementation_constraint import DeviceManagementSettingAbstractImplementationConstraint
        from .device_management_setting_app_constraint import DeviceManagementSettingAppConstraint
        from .device_management_setting_boolean_constraint import DeviceManagementSettingBooleanConstraint
        from .device_management_setting_collection_constraint import DeviceManagementSettingCollectionConstraint
        from .device_management_setting_enrollment_type_constraint import DeviceManagementSettingEnrollmentTypeConstraint
        from .device_management_setting_file_constraint import DeviceManagementSettingFileConstraint
        from .device_management_setting_integer_constraint import DeviceManagementSettingIntegerConstraint
        from .device_management_setting_profile_constraint import DeviceManagementSettingProfileConstraint
        from .device_management_setting_regex_constraint import DeviceManagementSettingRegexConstraint
        from .device_management_setting_required_constraint import DeviceManagementSettingRequiredConstraint
        from .device_management_setting_sddl_constraint import DeviceManagementSettingSddlConstraint
        from .device_management_setting_string_length_constraint import DeviceManagementSettingStringLengthConstraint
        from .device_management_setting_xml_constraint import DeviceManagementSettingXmlConstraint

        fields: Dict[str, Callable[[Any], None]] = {
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

