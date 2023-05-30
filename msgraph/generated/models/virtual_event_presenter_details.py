from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import item_body

class VirtualEventPresenterDetails(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new virtualEventPresenterDetails and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The bio property
        self._bio: Optional[item_body.ItemBody] = None
        # The company property
        self._company: Optional[str] = None
        # The jobTitle property
        self._job_title: Optional[str] = None
        # The linkedInProfileWebUrl property
        self._linked_in_profile_web_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The personalSiteWebUrl property
        self._personal_site_web_url: Optional[str] = None
        # The twitterProfileWebUrl property
        self._twitter_profile_web_url: Optional[str] = None
    
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
    
    @property
    def bio(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the bio property value. The bio property
        Returns: Optional[item_body.ItemBody]
        """
        return self._bio
    
    @bio.setter
    def bio(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the bio property value. The bio property
        Args:
            value: Value to set for the bio property.
        """
        self._bio = value
    
    @property
    def company(self,) -> Optional[str]:
        """
        Gets the company property value. The company property
        Returns: Optional[str]
        """
        return self._company
    
    @company.setter
    def company(self,value: Optional[str] = None) -> None:
        """
        Sets the company property value. The company property
        Args:
            value: Value to set for the company property.
        """
        self._company = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventPresenterDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventPresenterDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VirtualEventPresenterDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import item_body

        fields: Dict[str, Callable[[Any], None]] = {
            "bio": lambda n : setattr(self, 'bio', n.get_object_value(item_body.ItemBody)),
            "company": lambda n : setattr(self, 'company', n.get_str_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "linkedInProfileWebUrl": lambda n : setattr(self, 'linked_in_profile_web_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "personalSiteWebUrl": lambda n : setattr(self, 'personal_site_web_url', n.get_str_value()),
            "twitterProfileWebUrl": lambda n : setattr(self, 'twitter_profile_web_url', n.get_str_value()),
        }
        return fields
    
    @property
    def job_title(self,) -> Optional[str]:
        """
        Gets the jobTitle property value. The jobTitle property
        Returns: Optional[str]
        """
        return self._job_title
    
    @job_title.setter
    def job_title(self,value: Optional[str] = None) -> None:
        """
        Sets the jobTitle property value. The jobTitle property
        Args:
            value: Value to set for the job_title property.
        """
        self._job_title = value
    
    @property
    def linked_in_profile_web_url(self,) -> Optional[str]:
        """
        Gets the linkedInProfileWebUrl property value. The linkedInProfileWebUrl property
        Returns: Optional[str]
        """
        return self._linked_in_profile_web_url
    
    @linked_in_profile_web_url.setter
    def linked_in_profile_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the linkedInProfileWebUrl property value. The linkedInProfileWebUrl property
        Args:
            value: Value to set for the linked_in_profile_web_url property.
        """
        self._linked_in_profile_web_url = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def personal_site_web_url(self,) -> Optional[str]:
        """
        Gets the personalSiteWebUrl property value. The personalSiteWebUrl property
        Returns: Optional[str]
        """
        return self._personal_site_web_url
    
    @personal_site_web_url.setter
    def personal_site_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the personalSiteWebUrl property value. The personalSiteWebUrl property
        Args:
            value: Value to set for the personal_site_web_url property.
        """
        self._personal_site_web_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("bio", self.bio)
        writer.write_str_value("company", self.company)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_str_value("linkedInProfileWebUrl", self.linked_in_profile_web_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("personalSiteWebUrl", self.personal_site_web_url)
        writer.write_str_value("twitterProfileWebUrl", self.twitter_profile_web_url)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def twitter_profile_web_url(self,) -> Optional[str]:
        """
        Gets the twitterProfileWebUrl property value. The twitterProfileWebUrl property
        Returns: Optional[str]
        """
        return self._twitter_profile_web_url
    
    @twitter_profile_web_url.setter
    def twitter_profile_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the twitterProfileWebUrl property value. The twitterProfileWebUrl property
        Args:
            value: Value to set for the twitter_profile_web_url property.
        """
        self._twitter_profile_web_url = value
    

