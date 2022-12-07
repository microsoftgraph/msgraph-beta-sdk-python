from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

equivalent_content_option = lazy_import('msgraph.generated.models.windows_updates.equivalent_content_option')
quality_update_reference = lazy_import('msgraph.generated.models.windows_updates.quality_update_reference')

class ExpeditedQualityUpdateReference(quality_update_reference.QualityUpdateReference):
    def __init__(self,) -> None:
        """
        Instantiates a new ExpeditedQualityUpdateReference and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.expeditedQualityUpdateReference"
        # Specifies other content to consider as equivalent. Supports a subset of the values for equivalentContentOption. Default value is latestSecurity. Possible values are: latestSecurity, unknownFutureValue.
        self._equivalent_content: Optional[equivalent_content_option.EquivalentContentOption] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExpeditedQualityUpdateReference:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExpeditedQualityUpdateReference
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExpeditedQualityUpdateReference()
    
    @property
    def equivalent_content(self,) -> Optional[equivalent_content_option.EquivalentContentOption]:
        """
        Gets the equivalentContent property value. Specifies other content to consider as equivalent. Supports a subset of the values for equivalentContentOption. Default value is latestSecurity. Possible values are: latestSecurity, unknownFutureValue.
        Returns: Optional[equivalent_content_option.EquivalentContentOption]
        """
        return self._equivalent_content
    
    @equivalent_content.setter
    def equivalent_content(self,value: Optional[equivalent_content_option.EquivalentContentOption] = None) -> None:
        """
        Sets the equivalentContent property value. Specifies other content to consider as equivalent. Supports a subset of the values for equivalentContentOption. Default value is latestSecurity. Possible values are: latestSecurity, unknownFutureValue.
        Args:
            value: Value to set for the equivalentContent property.
        """
        self._equivalent_content = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "equivalent_content": lambda n : setattr(self, 'equivalent_content', n.get_enum_value(equivalent_content_option.EquivalentContentOption)),
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
        writer.write_enum_value("equivalentContent", self.equivalent_content)
    

