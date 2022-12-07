from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class MigrateToTemplatePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the migrateToTemplate method.
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
        Instantiates a new migrateToTemplatePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The newTemplateId property
        self._new_template_id: Optional[str] = None
        # The preserveCustomValues property
        self._preserve_custom_values: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MigrateToTemplatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MigrateToTemplatePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MigrateToTemplatePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "new_template_id": lambda n : setattr(self, 'new_template_id', n.get_str_value()),
            "preserve_custom_values": lambda n : setattr(self, 'preserve_custom_values', n.get_bool_value()),
        }
        return fields
    
    @property
    def new_template_id(self,) -> Optional[str]:
        """
        Gets the newTemplateId property value. The newTemplateId property
        Returns: Optional[str]
        """
        return self._new_template_id
    
    @new_template_id.setter
    def new_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the newTemplateId property value. The newTemplateId property
        Args:
            value: Value to set for the newTemplateId property.
        """
        self._new_template_id = value
    
    @property
    def preserve_custom_values(self,) -> Optional[bool]:
        """
        Gets the preserveCustomValues property value. The preserveCustomValues property
        Returns: Optional[bool]
        """
        return self._preserve_custom_values
    
    @preserve_custom_values.setter
    def preserve_custom_values(self,value: Optional[bool] = None) -> None:
        """
        Sets the preserveCustomValues property value. The preserveCustomValues property
        Args:
            value: Value to set for the preserveCustomValues property.
        """
        self._preserve_custom_values = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("newTemplateId", self.new_template_id)
        writer.write_bool_value("preserveCustomValues", self.preserve_custom_values)
        writer.write_additional_data_value(self.additional_data)
    

