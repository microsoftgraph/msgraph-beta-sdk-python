from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import case, case_operation, ediscovery_case_settings, ediscovery_custodian, ediscovery_hold_policy, ediscovery_noncustodial_data_source, ediscovery_review_set, ediscovery_review_tag, ediscovery_search
    from .. import identity_set

from . import case

class EdiscoveryCase(case.Case):
    def __init__(self,) -> None:
        """
        Instantiates a new EdiscoveryCase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.ediscoveryCase"
        # The user who closed the case.
        self._closed_by: Optional[identity_set.IdentitySet] = None
        # The date and time when the case was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._closed_date_time: Optional[datetime] = None
        # Returns a list of case ediscoveryCustodian objects for this case.
        self._custodians: Optional[List[ediscovery_custodian.EdiscoveryCustodian]] = None
        # The external case number for customer reference.
        self._external_id: Optional[str] = None
        # Returns a list of case eDiscoveryHoldPolicy objects for this case.
        self._legal_holds: Optional[List[ediscovery_hold_policy.EdiscoveryHoldPolicy]] = None
        # Returns a list of case ediscoveryNoncustodialDataSource objects for this case.
        self._noncustodial_data_sources: Optional[List[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource]] = None
        # Returns a list of case caseOperation objects for this case.
        self._operations: Optional[List[case_operation.CaseOperation]] = None
        # Returns a list of eDiscoveryReviewSet objects in the case.
        self._review_sets: Optional[List[ediscovery_review_set.EdiscoveryReviewSet]] = None
        # Returns a list of eDiscoverySearch objects associated with this case.
        self._searches: Optional[List[ediscovery_search.EdiscoverySearch]] = None
        # Returns a list of eDIscoverySettings objects in the case.
        self._settings: Optional[ediscovery_case_settings.EdiscoveryCaseSettings] = None
        # Returns a list of ediscoveryReviewTag objects associated to this case.
        self._tags: Optional[List[ediscovery_review_tag.EdiscoveryReviewTag]] = None
    
    @property
    def closed_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the closedBy property value. The user who closed the case.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._closed_by
    
    @closed_by.setter
    def closed_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the closedBy property value. The user who closed the case.
        Args:
            value: Value to set for the closed_by property.
        """
        self._closed_by = value
    
    @property
    def closed_date_time(self,) -> Optional[datetime]:
        """
        Gets the closedDateTime property value. The date and time when the case was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._closed_date_time
    
    @closed_date_time.setter
    def closed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the closedDateTime property value. The date and time when the case was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the closed_date_time property.
        """
        self._closed_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryCase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryCase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdiscoveryCase()
    
    @property
    def custodians(self,) -> Optional[List[ediscovery_custodian.EdiscoveryCustodian]]:
        """
        Gets the custodians property value. Returns a list of case ediscoveryCustodian objects for this case.
        Returns: Optional[List[ediscovery_custodian.EdiscoveryCustodian]]
        """
        return self._custodians
    
    @custodians.setter
    def custodians(self,value: Optional[List[ediscovery_custodian.EdiscoveryCustodian]] = None) -> None:
        """
        Sets the custodians property value. Returns a list of case ediscoveryCustodian objects for this case.
        Args:
            value: Value to set for the custodians property.
        """
        self._custodians = value
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. The external case number for customer reference.
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. The external case number for customer reference.
        Args:
            value: Value to set for the external_id property.
        """
        self._external_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import case, case_operation, ediscovery_case_settings, ediscovery_custodian, ediscovery_hold_policy, ediscovery_noncustodial_data_source, ediscovery_review_set, ediscovery_review_tag, ediscovery_search
        from .. import identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "closedBy": lambda n : setattr(self, 'closed_by', n.get_object_value(identity_set.IdentitySet)),
            "closedDateTime": lambda n : setattr(self, 'closed_date_time', n.get_datetime_value()),
            "custodians": lambda n : setattr(self, 'custodians', n.get_collection_of_object_values(ediscovery_custodian.EdiscoveryCustodian)),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "legalHolds": lambda n : setattr(self, 'legal_holds', n.get_collection_of_object_values(ediscovery_hold_policy.EdiscoveryHoldPolicy)),
            "noncustodialDataSources": lambda n : setattr(self, 'noncustodial_data_sources', n.get_collection_of_object_values(ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(case_operation.CaseOperation)),
            "reviewSets": lambda n : setattr(self, 'review_sets', n.get_collection_of_object_values(ediscovery_review_set.EdiscoveryReviewSet)),
            "searches": lambda n : setattr(self, 'searches', n.get_collection_of_object_values(ediscovery_search.EdiscoverySearch)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(ediscovery_case_settings.EdiscoveryCaseSettings)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(ediscovery_review_tag.EdiscoveryReviewTag)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def legal_holds(self,) -> Optional[List[ediscovery_hold_policy.EdiscoveryHoldPolicy]]:
        """
        Gets the legalHolds property value. Returns a list of case eDiscoveryHoldPolicy objects for this case.
        Returns: Optional[List[ediscovery_hold_policy.EdiscoveryHoldPolicy]]
        """
        return self._legal_holds
    
    @legal_holds.setter
    def legal_holds(self,value: Optional[List[ediscovery_hold_policy.EdiscoveryHoldPolicy]] = None) -> None:
        """
        Sets the legalHolds property value. Returns a list of case eDiscoveryHoldPolicy objects for this case.
        Args:
            value: Value to set for the legal_holds property.
        """
        self._legal_holds = value
    
    @property
    def noncustodial_data_sources(self,) -> Optional[List[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource]]:
        """
        Gets the noncustodialDataSources property value. Returns a list of case ediscoveryNoncustodialDataSource objects for this case.
        Returns: Optional[List[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource]]
        """
        return self._noncustodial_data_sources
    
    @noncustodial_data_sources.setter
    def noncustodial_data_sources(self,value: Optional[List[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource]] = None) -> None:
        """
        Sets the noncustodialDataSources property value. Returns a list of case ediscoveryNoncustodialDataSource objects for this case.
        Args:
            value: Value to set for the noncustodial_data_sources property.
        """
        self._noncustodial_data_sources = value
    
    @property
    def operations(self,) -> Optional[List[case_operation.CaseOperation]]:
        """
        Gets the operations property value. Returns a list of case caseOperation objects for this case.
        Returns: Optional[List[case_operation.CaseOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[case_operation.CaseOperation]] = None) -> None:
        """
        Sets the operations property value. Returns a list of case caseOperation objects for this case.
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def review_sets(self,) -> Optional[List[ediscovery_review_set.EdiscoveryReviewSet]]:
        """
        Gets the reviewSets property value. Returns a list of eDiscoveryReviewSet objects in the case.
        Returns: Optional[List[ediscovery_review_set.EdiscoveryReviewSet]]
        """
        return self._review_sets
    
    @review_sets.setter
    def review_sets(self,value: Optional[List[ediscovery_review_set.EdiscoveryReviewSet]] = None) -> None:
        """
        Sets the reviewSets property value. Returns a list of eDiscoveryReviewSet objects in the case.
        Args:
            value: Value to set for the review_sets property.
        """
        self._review_sets = value
    
    @property
    def searches(self,) -> Optional[List[ediscovery_search.EdiscoverySearch]]:
        """
        Gets the searches property value. Returns a list of eDiscoverySearch objects associated with this case.
        Returns: Optional[List[ediscovery_search.EdiscoverySearch]]
        """
        return self._searches
    
    @searches.setter
    def searches(self,value: Optional[List[ediscovery_search.EdiscoverySearch]] = None) -> None:
        """
        Sets the searches property value. Returns a list of eDiscoverySearch objects associated with this case.
        Args:
            value: Value to set for the searches property.
        """
        self._searches = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("closedBy", self.closed_by)
        writer.write_datetime_value("closedDateTime", self.closed_date_time)
        writer.write_collection_of_object_values("custodians", self.custodians)
        writer.write_str_value("externalId", self.external_id)
        writer.write_collection_of_object_values("legalHolds", self.legal_holds)
        writer.write_collection_of_object_values("noncustodialDataSources", self.noncustodial_data_sources)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("reviewSets", self.review_sets)
        writer.write_collection_of_object_values("searches", self.searches)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("tags", self.tags)
    
    @property
    def settings(self,) -> Optional[ediscovery_case_settings.EdiscoveryCaseSettings]:
        """
        Gets the settings property value. Returns a list of eDIscoverySettings objects in the case.
        Returns: Optional[ediscovery_case_settings.EdiscoveryCaseSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[ediscovery_case_settings.EdiscoveryCaseSettings] = None) -> None:
        """
        Sets the settings property value. Returns a list of eDIscoverySettings objects in the case.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def tags(self,) -> Optional[List[ediscovery_review_tag.EdiscoveryReviewTag]]:
        """
        Gets the tags property value. Returns a list of ediscoveryReviewTag objects associated to this case.
        Returns: Optional[List[ediscovery_review_tag.EdiscoveryReviewTag]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[ediscovery_review_tag.EdiscoveryReviewTag]] = None) -> None:
        """
        Sets the tags property value. Returns a list of ediscoveryReviewTag objects associated to this case.
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    

