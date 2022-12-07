from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

content_properties = lazy_import('msgraph.generated.models.content_properties')
dlp_evaluation_input = lazy_import('msgraph.generated.models.dlp_evaluation_input')

class DlpEvaluationWindowsDevicesInput(dlp_evaluation_input.DlpEvaluationInput):
    def __init__(self,) -> None:
        """
        Instantiates a new DlpEvaluationWindowsDevicesInput and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.dlpEvaluationWindowsDevicesInput"
        # The contentProperties property
        self._content_properties: Optional[content_properties.ContentProperties] = None
        # The sharedBy property
        self._shared_by: Optional[str] = None
    
    @property
    def content_properties(self,) -> Optional[content_properties.ContentProperties]:
        """
        Gets the contentProperties property value. The contentProperties property
        Returns: Optional[content_properties.ContentProperties]
        """
        return self._content_properties
    
    @content_properties.setter
    def content_properties(self,value: Optional[content_properties.ContentProperties] = None) -> None:
        """
        Sets the contentProperties property value. The contentProperties property
        Args:
            value: Value to set for the contentProperties property.
        """
        self._content_properties = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DlpEvaluationWindowsDevicesInput:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DlpEvaluationWindowsDevicesInput
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DlpEvaluationWindowsDevicesInput()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content_properties": lambda n : setattr(self, 'content_properties', n.get_object_value(content_properties.ContentProperties)),
            "shared_by": lambda n : setattr(self, 'shared_by', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("contentProperties", self.content_properties)
        writer.write_str_value("sharedBy", self.shared_by)
    
    @property
    def shared_by(self,) -> Optional[str]:
        """
        Gets the sharedBy property value. The sharedBy property
        Returns: Optional[str]
        """
        return self._shared_by
    
    @shared_by.setter
    def shared_by(self,value: Optional[str] = None) -> None:
        """
        Sets the sharedBy property value. The sharedBy property
        Args:
            value: Value to set for the sharedBy property.
        """
        self._shared_by = value
    

