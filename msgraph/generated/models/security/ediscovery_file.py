from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ediscovery_custodian = lazy_import('msgraph.generated.models.security.ediscovery_custodian')
ediscovery_review_tag = lazy_import('msgraph.generated.models.security.ediscovery_review_tag')
file = lazy_import('msgraph.generated.models.security.file')

class EdiscoveryFile(file.File):
    def __init__(self,) -> None:
        """
        Instantiates a new EdiscoveryFile and sets the default values.
        """
        super().__init__()
        # Custodians associated with the file.
        self._custodian: Optional[ediscovery_custodian.EdiscoveryCustodian] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Tags associated with the file.
        self._tags: Optional[List[ediscovery_review_tag.EdiscoveryReviewTag]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryFile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdiscoveryFile()
    
    @property
    def custodian(self,) -> Optional[ediscovery_custodian.EdiscoveryCustodian]:
        """
        Gets the custodian property value. Custodians associated with the file.
        Returns: Optional[ediscovery_custodian.EdiscoveryCustodian]
        """
        return self._custodian
    
    @custodian.setter
    def custodian(self,value: Optional[ediscovery_custodian.EdiscoveryCustodian] = None) -> None:
        """
        Sets the custodian property value. Custodians associated with the file.
        Args:
            value: Value to set for the custodian property.
        """
        self._custodian = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "custodian": lambda n : setattr(self, 'custodian', n.get_object_value(ediscovery_custodian.EdiscoveryCustodian)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(ediscovery_review_tag.EdiscoveryReviewTag)),
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
        writer.write_object_value("custodian", self.custodian)
        writer.write_collection_of_object_values("tags", self.tags)
    
    @property
    def tags(self,) -> Optional[List[ediscovery_review_tag.EdiscoveryReviewTag]]:
        """
        Gets the tags property value. Tags associated with the file.
        Returns: Optional[List[ediscovery_review_tag.EdiscoveryReviewTag]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[ediscovery_review_tag.EdiscoveryReviewTag]] = None) -> None:
        """
        Sets the tags property value. Tags associated with the file.
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    

