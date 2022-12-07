from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

management_template_detailed_info = lazy_import('msgraph.generated.models.managed_tenants.management_template_detailed_info')

class ManagementIntentInfo(AdditionalDataHolder, Parsable):
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
        Instantiates a new managementIntentInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The display name for the management intent. Optional. Read-only.
        self._management_intent_display_name: Optional[str] = None
        # The identifier for the management intent. Required. Read-only.
        self._management_intent_id: Optional[str] = None
        # The collection of management template information associated with the management intent. Optional. Read-only.
        self._management_templates: Optional[List[management_template_detailed_info.ManagementTemplateDetailedInfo]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementIntentInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementIntentInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagementIntentInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "management_intent_display_name": lambda n : setattr(self, 'management_intent_display_name', n.get_str_value()),
            "management_intent_id": lambda n : setattr(self, 'management_intent_id', n.get_str_value()),
            "management_templates": lambda n : setattr(self, 'management_templates', n.get_collection_of_object_values(management_template_detailed_info.ManagementTemplateDetailedInfo)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def management_intent_display_name(self,) -> Optional[str]:
        """
        Gets the managementIntentDisplayName property value. The display name for the management intent. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._management_intent_display_name
    
    @management_intent_display_name.setter
    def management_intent_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the managementIntentDisplayName property value. The display name for the management intent. Optional. Read-only.
        Args:
            value: Value to set for the managementIntentDisplayName property.
        """
        self._management_intent_display_name = value
    
    @property
    def management_intent_id(self,) -> Optional[str]:
        """
        Gets the managementIntentId property value. The identifier for the management intent. Required. Read-only.
        Returns: Optional[str]
        """
        return self._management_intent_id
    
    @management_intent_id.setter
    def management_intent_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managementIntentId property value. The identifier for the management intent. Required. Read-only.
        Args:
            value: Value to set for the managementIntentId property.
        """
        self._management_intent_id = value
    
    @property
    def management_templates(self,) -> Optional[List[management_template_detailed_info.ManagementTemplateDetailedInfo]]:
        """
        Gets the managementTemplates property value. The collection of management template information associated with the management intent. Optional. Read-only.
        Returns: Optional[List[management_template_detailed_info.ManagementTemplateDetailedInfo]]
        """
        return self._management_templates
    
    @management_templates.setter
    def management_templates(self,value: Optional[List[management_template_detailed_info.ManagementTemplateDetailedInfo]] = None) -> None:
        """
        Sets the managementTemplates property value. The collection of management template information associated with the management intent. Optional. Read-only.
        Args:
            value: Value to set for the managementTemplates property.
        """
        self._management_templates = value
    
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
        writer.write_str_value("managementIntentDisplayName", self.management_intent_display_name)
        writer.write_str_value("managementIntentId", self.management_intent_id)
        writer.write_collection_of_object_values("managementTemplates", self.management_templates)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

