from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import article_indicator, artifact, indicator_source, intelligence_profile_indicator
    from .. import entity

from .. import entity

@dataclass
class Indicator(entity.Entity):
    # The artifact property
    artifact: Optional[artifact.Artifact] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The source property
    source: Optional[indicator_source.IndicatorSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Indicator:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Indicator
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.articleIndicator".casefold():
            from . import article_indicator

            return article_indicator.ArticleIndicator()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.intelligenceProfileIndicator".casefold():
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("artifact", self.artifact)
        writer.write_enum_value("source", self.source)
    

