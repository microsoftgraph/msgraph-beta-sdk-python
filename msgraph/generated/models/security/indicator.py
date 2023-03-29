from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import article_indicator, artifact, indicator_source, intelligence_profile_indicator
    from .. import entity

from .. import entity

class Indicator(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new indicator and sets the default values.
        """
        super().__init__()
        # The artifact property
        self._artifact: Optional[artifact.Artifact] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The source property
        self._source: Optional[indicator_source.IndicatorSource] = None
    
    @property
    def artifact(self,) -> Optional[artifact.Artifact]:
        """
        Gets the artifact property value. The artifact property
        Returns: Optional[artifact.Artifact]
        """
        return self._artifact
    
    @artifact.setter
    def artifact(self,value: Optional[artifact.Artifact] = None) -> None:
        """
        Sets the artifact property value. The artifact property
        Args:
            value: Value to set for the artifact property.
        """
        self._artifact = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Indicator:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Indicator
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.security.articleIndicator":
                from . import article_indicator

                return article_indicator.ArticleIndicator()
            if mapping_value == "#microsoft.graph.security.intelligenceProfileIndicator":
                from . import intelligence_profile_indicator

                return intelligence_profile_indicator.IntelligenceProfileIndicator()
        return Indicator()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import article_indicator, artifact, indicator_source, intelligence_profile_indicator
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "artifact": lambda n : setattr(self, 'artifact', n.get_object_value(artifact.Artifact)),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(indicator_source.IndicatorSource)),
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
        writer.write_object_value("artifact", self.artifact)
        writer.write_enum_value("source", self.source)
    
    @property
    def source(self,) -> Optional[indicator_source.IndicatorSource]:
        """
        Gets the source property value. The source property
        Returns: Optional[indicator_source.IndicatorSource]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[indicator_source.IndicatorSource] = None) -> None:
        """
        Sets the source property value. The source property
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    

