from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
information_protection_policy_setting = lazy_import('msgraph.generated.models.security.information_protection_policy_setting')
sensitivity_label = lazy_import('msgraph.generated.models.security.sensitivity_label')

class InformationProtection(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new informationProtection and sets the default values.
        """
        super().__init__()
        # Read the Microsoft Purview Information Protection policy settings for the user or organization.
        self._label_policy_settings: Optional[information_protection_policy_setting.InformationProtectionPolicySetting] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Read the Microsoft Purview Information Protection labels for the user or organization.
        self._sensitivity_labels: Optional[List[sensitivity_label.SensitivityLabel]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InformationProtection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "label_policy_settings": lambda n : setattr(self, 'label_policy_settings', n.get_object_value(information_protection_policy_setting.InformationProtectionPolicySetting)),
            "sensitivity_labels": lambda n : setattr(self, 'sensitivity_labels', n.get_collection_of_object_values(sensitivity_label.SensitivityLabel)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def label_policy_settings(self,) -> Optional[information_protection_policy_setting.InformationProtectionPolicySetting]:
        """
        Gets the labelPolicySettings property value. Read the Microsoft Purview Information Protection policy settings for the user or organization.
        Returns: Optional[information_protection_policy_setting.InformationProtectionPolicySetting]
        """
        return self._label_policy_settings
    
    @label_policy_settings.setter
    def label_policy_settings(self,value: Optional[information_protection_policy_setting.InformationProtectionPolicySetting] = None) -> None:
        """
        Sets the labelPolicySettings property value. Read the Microsoft Purview Information Protection policy settings for the user or organization.
        Args:
            value: Value to set for the labelPolicySettings property.
        """
        self._label_policy_settings = value
    
    @property
    def sensitivity_labels(self,) -> Optional[List[sensitivity_label.SensitivityLabel]]:
        """
        Gets the sensitivityLabels property value. Read the Microsoft Purview Information Protection labels for the user or organization.
        Returns: Optional[List[sensitivity_label.SensitivityLabel]]
        """
        return self._sensitivity_labels
    
    @sensitivity_labels.setter
    def sensitivity_labels(self,value: Optional[List[sensitivity_label.SensitivityLabel]] = None) -> None:
        """
        Sets the sensitivityLabels property value. Read the Microsoft Purview Information Protection labels for the user or organization.
        Args:
            value: Value to set for the sensitivityLabels property.
        """
        self._sensitivity_labels = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("labelPolicySettings", self.label_policy_settings)
        writer.write_collection_of_object_values("sensitivityLabels", self.sensitivity_labels)
    

