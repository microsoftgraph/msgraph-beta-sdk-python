from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
sensitivity_label_target = lazy_import('msgraph.generated.models.sensitivity_label_target')

class SensitivityPolicySettings(entity.Entity):
    @property
    def applicable_to(self,) -> Optional[sensitivity_label_target.SensitivityLabelTarget]:
        """
        Gets the applicableTo property value. The applicableTo property
        Returns: Optional[sensitivity_label_target.SensitivityLabelTarget]
        """
        return self._applicable_to
    
    @applicable_to.setter
    def applicable_to(self,value: Optional[sensitivity_label_target.SensitivityLabelTarget] = None) -> None:
        """
        Sets the applicableTo property value. The applicableTo property
        Args:
            value: Value to set for the applicableTo property.
        """
        self._applicable_to = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new sensitivityPolicySettings and sets the default values.
        """
        super().__init__()
        # The applicableTo property
        self._applicable_to: Optional[sensitivity_label_target.SensitivityLabelTarget] = None
        # The downgradeSensitivityRequiresJustification property
        self._downgrade_sensitivity_requires_justification: Optional[bool] = None
        # The helpWebUrl property
        self._help_web_url: Optional[str] = None
        # The isMandatory property
        self._is_mandatory: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SensitivityPolicySettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SensitivityPolicySettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SensitivityPolicySettings()
    
    @property
    def downgrade_sensitivity_requires_justification(self,) -> Optional[bool]:
        """
        Gets the downgradeSensitivityRequiresJustification property value. The downgradeSensitivityRequiresJustification property
        Returns: Optional[bool]
        """
        return self._downgrade_sensitivity_requires_justification
    
    @downgrade_sensitivity_requires_justification.setter
    def downgrade_sensitivity_requires_justification(self,value: Optional[bool] = None) -> None:
        """
        Sets the downgradeSensitivityRequiresJustification property value. The downgradeSensitivityRequiresJustification property
        Args:
            value: Value to set for the downgradeSensitivityRequiresJustification property.
        """
        self._downgrade_sensitivity_requires_justification = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applicable_to": lambda n : setattr(self, 'applicable_to', n.get_enum_value(sensitivity_label_target.SensitivityLabelTarget)),
            "downgrade_sensitivity_requires_justification": lambda n : setattr(self, 'downgrade_sensitivity_requires_justification', n.get_bool_value()),
            "help_web_url": lambda n : setattr(self, 'help_web_url', n.get_str_value()),
            "is_mandatory": lambda n : setattr(self, 'is_mandatory', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def help_web_url(self,) -> Optional[str]:
        """
        Gets the helpWebUrl property value. The helpWebUrl property
        Returns: Optional[str]
        """
        return self._help_web_url
    
    @help_web_url.setter
    def help_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the helpWebUrl property value. The helpWebUrl property
        Args:
            value: Value to set for the helpWebUrl property.
        """
        self._help_web_url = value
    
    @property
    def is_mandatory(self,) -> Optional[bool]:
        """
        Gets the isMandatory property value. The isMandatory property
        Returns: Optional[bool]
        """
        return self._is_mandatory
    
    @is_mandatory.setter
    def is_mandatory(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMandatory property value. The isMandatory property
        Args:
            value: Value to set for the isMandatory property.
        """
        self._is_mandatory = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("applicableTo", self.applicable_to)
        writer.write_bool_value("downgradeSensitivityRequiresJustification", self.downgrade_sensitivity_requires_justification)
        writer.write_str_value("helpWebUrl", self.help_web_url)
        writer.write_bool_value("isMandatory", self.is_mandatory)
    

