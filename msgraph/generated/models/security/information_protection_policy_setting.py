from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class InformationProtectionPolicySetting(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new informationProtectionPolicySetting and sets the default values.
        """
        super().__init__()
        # The defaultLabelId property
        self._default_label_id: Optional[str] = None
        # Exposes whether justification input is required on label downgrade.
        self._is_downgrade_justification_required: Optional[bool] = None
        # Exposes whether mandatory labeling is enabled.
        self._is_mandatory: Optional[bool] = None
        # Exposes the more information URL that can be configured by the administrator.
        self._more_info_url: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationProtectionPolicySetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtectionPolicySetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InformationProtectionPolicySetting()
    
    @property
    def default_label_id(self,) -> Optional[str]:
        """
        Gets the defaultLabelId property value. The defaultLabelId property
        Returns: Optional[str]
        """
        return self._default_label_id
    
    @default_label_id.setter
    def default_label_id(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultLabelId property value. The defaultLabelId property
        Args:
            value: Value to set for the defaultLabelId property.
        """
        self._default_label_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_label_id": lambda n : setattr(self, 'default_label_id', n.get_str_value()),
            "is_downgrade_justification_required": lambda n : setattr(self, 'is_downgrade_justification_required', n.get_bool_value()),
            "is_mandatory": lambda n : setattr(self, 'is_mandatory', n.get_bool_value()),
            "more_info_url": lambda n : setattr(self, 'more_info_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_downgrade_justification_required(self,) -> Optional[bool]:
        """
        Gets the isDowngradeJustificationRequired property value. Exposes whether justification input is required on label downgrade.
        Returns: Optional[bool]
        """
        return self._is_downgrade_justification_required
    
    @is_downgrade_justification_required.setter
    def is_downgrade_justification_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDowngradeJustificationRequired property value. Exposes whether justification input is required on label downgrade.
        Args:
            value: Value to set for the isDowngradeJustificationRequired property.
        """
        self._is_downgrade_justification_required = value
    
    @property
    def is_mandatory(self,) -> Optional[bool]:
        """
        Gets the isMandatory property value. Exposes whether mandatory labeling is enabled.
        Returns: Optional[bool]
        """
        return self._is_mandatory
    
    @is_mandatory.setter
    def is_mandatory(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMandatory property value. Exposes whether mandatory labeling is enabled.
        Args:
            value: Value to set for the isMandatory property.
        """
        self._is_mandatory = value
    
    @property
    def more_info_url(self,) -> Optional[str]:
        """
        Gets the moreInfoUrl property value. Exposes the more information URL that can be configured by the administrator.
        Returns: Optional[str]
        """
        return self._more_info_url
    
    @more_info_url.setter
    def more_info_url(self,value: Optional[str] = None) -> None:
        """
        Sets the moreInfoUrl property value. Exposes the more information URL that can be configured by the administrator.
        Args:
            value: Value to set for the moreInfoUrl property.
        """
        self._more_info_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("defaultLabelId", self.default_label_id)
        writer.write_bool_value("isDowngradeJustificationRequired", self.is_downgrade_justification_required)
        writer.write_bool_value("isMandatory", self.is_mandatory)
        writer.write_str_value("moreInfoUrl", self.more_info_url)
    

