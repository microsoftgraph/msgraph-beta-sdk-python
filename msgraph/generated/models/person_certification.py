from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_facet = lazy_import('msgraph.generated.models.item_facet')

class PersonCertification(item_facet.ItemFacet):
    @property
    def certification_id(self,) -> Optional[str]:
        """
        Gets the certificationId property value. The referenceable identifier for the certification.
        Returns: Optional[str]
        """
        return self._certification_id
    
    @certification_id.setter
    def certification_id(self,value: Optional[str] = None) -> None:
        """
        Sets the certificationId property value. The referenceable identifier for the certification.
        Args:
            value: Value to set for the certificationId property.
        """
        self._certification_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new PersonCertification and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.personCertification"
        # The referenceable identifier for the certification.
        self._certification_id: Optional[str] = None
        # Description of the certification.
        self._description: Optional[str] = None
        # Title of the certification.
        self._display_name: Optional[str] = None
        # The date that the certification expires.
        self._end_date: Optional[Date] = None
        # The date that the certification was issued.
        self._issued_date: Optional[Date] = None
        # Authority which granted the certification.
        self._issuing_authority: Optional[str] = None
        # Company which granted the certification.
        self._issuing_company: Optional[str] = None
        # The date that the certification became valid.
        self._start_date: Optional[Date] = None
        # URL referencing a thumbnail of the certification.
        self._thumbnail_url: Optional[str] = None
        # URL referencing the certification.
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PersonCertification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PersonCertification
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PersonCertification()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the certification.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the certification.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Title of the certification.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Title of the certification.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def end_date(self,) -> Optional[Date]:
        """
        Gets the endDate property value. The date that the certification expires.
        Returns: Optional[Date]
        """
        return self._end_date
    
    @end_date.setter
    def end_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the endDate property value. The date that the certification expires.
        Args:
            value: Value to set for the endDate property.
        """
        self._end_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "certification_id": lambda n : setattr(self, 'certification_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "end_date": lambda n : setattr(self, 'end_date', n.get_object_value(Date)),
            "issued_date": lambda n : setattr(self, 'issued_date', n.get_object_value(Date)),
            "issuing_authority": lambda n : setattr(self, 'issuing_authority', n.get_str_value()),
            "issuing_company": lambda n : setattr(self, 'issuing_company', n.get_str_value()),
            "start_date": lambda n : setattr(self, 'start_date', n.get_object_value(Date)),
            "thumbnail_url": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def issued_date(self,) -> Optional[Date]:
        """
        Gets the issuedDate property value. The date that the certification was issued.
        Returns: Optional[Date]
        """
        return self._issued_date
    
    @issued_date.setter
    def issued_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the issuedDate property value. The date that the certification was issued.
        Args:
            value: Value to set for the issuedDate property.
        """
        self._issued_date = value
    
    @property
    def issuing_authority(self,) -> Optional[str]:
        """
        Gets the issuingAuthority property value. Authority which granted the certification.
        Returns: Optional[str]
        """
        return self._issuing_authority
    
    @issuing_authority.setter
    def issuing_authority(self,value: Optional[str] = None) -> None:
        """
        Sets the issuingAuthority property value. Authority which granted the certification.
        Args:
            value: Value to set for the issuingAuthority property.
        """
        self._issuing_authority = value
    
    @property
    def issuing_company(self,) -> Optional[str]:
        """
        Gets the issuingCompany property value. Company which granted the certification.
        Returns: Optional[str]
        """
        return self._issuing_company
    
    @issuing_company.setter
    def issuing_company(self,value: Optional[str] = None) -> None:
        """
        Sets the issuingCompany property value. Company which granted the certification.
        Args:
            value: Value to set for the issuingCompany property.
        """
        self._issuing_company = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("certificationId", self.certification_id)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("endDate", self.end_date)
        writer.write_object_value("issuedDate", self.issued_date)
        writer.write_str_value("issuingAuthority", self.issuing_authority)
        writer.write_str_value("issuingCompany", self.issuing_company)
        writer.write_object_value("startDate", self.start_date)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def start_date(self,) -> Optional[Date]:
        """
        Gets the startDate property value. The date that the certification became valid.
        Returns: Optional[Date]
        """
        return self._start_date
    
    @start_date.setter
    def start_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the startDate property value. The date that the certification became valid.
        Args:
            value: Value to set for the startDate property.
        """
        self._start_date = value
    
    @property
    def thumbnail_url(self,) -> Optional[str]:
        """
        Gets the thumbnailUrl property value. URL referencing a thumbnail of the certification.
        Returns: Optional[str]
        """
        return self._thumbnail_url
    
    @thumbnail_url.setter
    def thumbnail_url(self,value: Optional[str] = None) -> None:
        """
        Sets the thumbnailUrl property value. URL referencing a thumbnail of the certification.
        Args:
            value: Value to set for the thumbnailUrl property.
        """
        self._thumbnail_url = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. URL referencing the certification.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. URL referencing the certification.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

