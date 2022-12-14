from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
section_emphasis_type = lazy_import('msgraph.generated.models.section_emphasis_type')
web_part = lazy_import('msgraph.generated.models.web_part')

class VerticalSection(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new verticalSection and sets the default values.
        """
        super().__init__()
        # Enumeration value that indicates the emphasis of the section background. The possible values are: none, netural, soft, strong, unknownFutureValue.
        self._emphasis: Optional[section_emphasis_type.SectionEmphasisType] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The set of web parts in this section.
        self._webparts: Optional[List[web_part.WebPart]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VerticalSection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VerticalSection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VerticalSection()
    
    @property
    def emphasis(self,) -> Optional[section_emphasis_type.SectionEmphasisType]:
        """
        Gets the emphasis property value. Enumeration value that indicates the emphasis of the section background. The possible values are: none, netural, soft, strong, unknownFutureValue.
        Returns: Optional[section_emphasis_type.SectionEmphasisType]
        """
        return self._emphasis
    
    @emphasis.setter
    def emphasis(self,value: Optional[section_emphasis_type.SectionEmphasisType] = None) -> None:
        """
        Sets the emphasis property value. Enumeration value that indicates the emphasis of the section background. The possible values are: none, netural, soft, strong, unknownFutureValue.
        Args:
            value: Value to set for the emphasis property.
        """
        self._emphasis = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "emphasis": lambda n : setattr(self, 'emphasis', n.get_enum_value(section_emphasis_type.SectionEmphasisType)),
            "webparts": lambda n : setattr(self, 'webparts', n.get_collection_of_object_values(web_part.WebPart)),
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
        writer.write_enum_value("emphasis", self.emphasis)
        writer.write_collection_of_object_values("webparts", self.webparts)
    
    @property
    def webparts(self,) -> Optional[List[web_part.WebPart]]:
        """
        Gets the webparts property value. The set of web parts in this section.
        Returns: Optional[List[web_part.WebPart]]
        """
        return self._webparts
    
    @webparts.setter
    def webparts(self,value: Optional[List[web_part.WebPart]] = None) -> None:
        """
        Sets the webparts property value. The set of web parts in this section.
        Args:
            value: Value to set for the webparts property.
        """
        self._webparts = value
    

