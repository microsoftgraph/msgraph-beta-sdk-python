from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_template_family = lazy_import('msgraph.generated.models.device_management_configuration_template_family')

class DeviceManagementConfigurationPolicyTemplateReference(AdditionalDataHolder, Parsable):
    """
    Policy template reference information
    """
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationPolicyTemplateReference and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Template Display Name of the referenced template. This property is read-only.
        self._template_display_name: Optional[str] = None
        # Template Display Version of the referenced Template. This property is read-only.
        self._template_display_version: Optional[str] = None
        # Describes the TemplateFamily for the Template entity
        self._template_family: Optional[device_management_configuration_template_family.DeviceManagementConfigurationTemplateFamily] = None
        # Template id
        self._template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationPolicyTemplateReference:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationPolicyTemplateReference
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationPolicyTemplateReference()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "template_display_name": lambda n : setattr(self, 'template_display_name', n.get_str_value()),
            "template_display_version": lambda n : setattr(self, 'template_display_version', n.get_str_value()),
            "template_family": lambda n : setattr(self, 'template_family', n.get_enum_value(device_management_configuration_template_family.DeviceManagementConfigurationTemplateFamily)),
            "template_id": lambda n : setattr(self, 'template_id', n.get_str_value()),
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
            value: Value to set for the OdataType property.
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
        writer.write_enum_value("templateFamily", self.template_family)
        writer.write_str_value("templateId", self.template_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def template_display_name(self,) -> Optional[str]:
        """
        Gets the templateDisplayName property value. Template Display Name of the referenced template. This property is read-only.
        Returns: Optional[str]
        """
        return self._template_display_name
    
    @template_display_name.setter
    def template_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the templateDisplayName property value. Template Display Name of the referenced template. This property is read-only.
        Args:
            value: Value to set for the templateDisplayName property.
        """
        self._template_display_name = value
    
    @property
    def template_display_version(self,) -> Optional[str]:
        """
        Gets the templateDisplayVersion property value. Template Display Version of the referenced Template. This property is read-only.
        Returns: Optional[str]
        """
        return self._template_display_version
    
    @template_display_version.setter
    def template_display_version(self,value: Optional[str] = None) -> None:
        """
        Sets the templateDisplayVersion property value. Template Display Version of the referenced Template. This property is read-only.
        Args:
            value: Value to set for the templateDisplayVersion property.
        """
        self._template_display_version = value
    
    @property
    def template_family(self,) -> Optional[device_management_configuration_template_family.DeviceManagementConfigurationTemplateFamily]:
        """
        Gets the templateFamily property value. Describes the TemplateFamily for the Template entity
        Returns: Optional[device_management_configuration_template_family.DeviceManagementConfigurationTemplateFamily]
        """
        return self._template_family
    
    @template_family.setter
    def template_family(self,value: Optional[device_management_configuration_template_family.DeviceManagementConfigurationTemplateFamily] = None) -> None:
        """
        Sets the templateFamily property value. Describes the TemplateFamily for the Template entity
        Args:
            value: Value to set for the templateFamily property.
        """
        self._template_family = value
    
    @property
    def template_id(self,) -> Optional[str]:
        """
        Gets the templateId property value. Template id
        Returns: Optional[str]
        """
        return self._template_id
    
    @template_id.setter
    def template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the templateId property value. Template id
        Args:
            value: Value to set for the templateId property.
        """
        self._template_id = value
    

