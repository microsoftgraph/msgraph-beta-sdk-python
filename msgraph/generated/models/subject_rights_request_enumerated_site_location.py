from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import subject_rights_request_site_location

from . import subject_rights_request_site_location

class SubjectRightsRequestEnumeratedSiteLocation(subject_rights_request_site_location.SubjectRightsRequestSiteLocation):
    def __init__(self,) -> None:
        """
        Instantiates a new SubjectRightsRequestEnumeratedSiteLocation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.subjectRightsRequestEnumeratedSiteLocation"
        # Collection of site URLs that should be included. Includes the URL of each site, for example, https://www.contoso.com/site1.
        self._urls: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubjectRightsRequestEnumeratedSiteLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequestEnumeratedSiteLocation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SubjectRightsRequestEnumeratedSiteLocation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import subject_rights_request_site_location

        fields: Dict[str, Callable[[Any], None]] = {
            "urls": lambda n : setattr(self, 'urls', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("urls", self.urls)
    
    @property
    def urls(self,) -> Optional[List[str]]:
        """
        Gets the urls property value. Collection of site URLs that should be included. Includes the URL of each site, for example, https://www.contoso.com/site1.
        Returns: Optional[List[str]]
        """
        return self._urls
    
    @urls.setter
    def urls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the urls property value. Collection of site URLs that should be included. Includes the URL of each site, for example, https://www.contoso.com/site1.
        Args:
            value: Value to set for the urls property.
        """
        self._urls = value
    

