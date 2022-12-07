from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_question = lazy_import('msgraph.generated.models.access_package_question')
access_package_resource_attribute_source = lazy_import('msgraph.generated.models.access_package_resource_attribute_source')

class AccessPackageResourceAttributeQuestion(access_package_resource_attribute_source.AccessPackageResourceAttributeSource):
    def __init__(self,) -> None:
        """
        Instantiates a new AccessPackageResourceAttributeQuestion and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.accessPackageResourceAttributeQuestion"
        # The question asked in order to get the value of the attribute
        self._question: Optional[access_package_question.AccessPackageQuestion] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageResourceAttributeQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceAttributeQuestion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageResourceAttributeQuestion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "question": lambda n : setattr(self, 'question', n.get_object_value(access_package_question.AccessPackageQuestion)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def question(self,) -> Optional[access_package_question.AccessPackageQuestion]:
        """
        Gets the question property value. The question asked in order to get the value of the attribute
        Returns: Optional[access_package_question.AccessPackageQuestion]
        """
        return self._question
    
    @question.setter
    def question(self,value: Optional[access_package_question.AccessPackageQuestion] = None) -> None:
        """
        Sets the question property value. The question asked in order to get the value of the attribute
        Args:
            value: Value to set for the question property.
        """
        self._question = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("question", self.question)
    

