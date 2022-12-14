from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authored_note = lazy_import('msgraph.generated.models.authored_note')
data_subject = lazy_import('msgraph.generated.models.data_subject')
data_subject_type = lazy_import('msgraph.generated.models.data_subject_type')
entity = lazy_import('msgraph.generated.models.entity')
identity = lazy_import('msgraph.generated.models.identity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
subject_rights_request_detail = lazy_import('msgraph.generated.models.subject_rights_request_detail')
subject_rights_request_history = lazy_import('msgraph.generated.models.subject_rights_request_history')
subject_rights_request_mailbox_location = lazy_import('msgraph.generated.models.subject_rights_request_mailbox_location')
subject_rights_request_site_location = lazy_import('msgraph.generated.models.subject_rights_request_site_location')
subject_rights_request_stage_detail = lazy_import('msgraph.generated.models.subject_rights_request_stage_detail')
subject_rights_request_status = lazy_import('msgraph.generated.models.subject_rights_request_status')
subject_rights_request_type = lazy_import('msgraph.generated.models.subject_rights_request_type')
team = lazy_import('msgraph.generated.models.team')

class SubjectRightsRequest(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def assigned_to(self,) -> Optional[identity.Identity]:
        """
        Gets the assignedTo property value. Identity that the request is assigned to.
        Returns: Optional[identity.Identity]
        """
        return self._assigned_to
    
    @assigned_to.setter
    def assigned_to(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the assignedTo property value. Identity that the request is assigned to.
        Args:
            value: Value to set for the assignedTo property.
        """
        self._assigned_to = value
    
    @property
    def closed_date_time(self,) -> Optional[datetime]:
        """
        Gets the closedDateTime property value. The date and time when the request was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._closed_date_time
    
    @closed_date_time.setter
    def closed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the closedDateTime property value. The date and time when the request was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the closedDateTime property.
        """
        self._closed_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new subjectRightsRequest and sets the default values.
        """
        super().__init__()
        # Identity that the request is assigned to.
        self._assigned_to: Optional[identity.Identity] = None
        # The date and time when the request was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._closed_date_time: Optional[datetime] = None
        # KQL based content query that should be used for search. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
        self._content_query: Optional[str] = None
        # Identity information for the entity that created the request.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The date and time when the request was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._created_date_time: Optional[datetime] = None
        # Information about the data subject.
        self._data_subject: Optional[data_subject.DataSubject] = None
        # The type of the data subject. Possible values are: customer, currentEmployee, formerEmployee, prospectiveEmployee, student, teacher, faculty, other, unknownFutureValue.
        self._data_subject_type: Optional[data_subject_type.DataSubjectType] = None
        # Description for the request.
        self._description: Optional[str] = None
        # The name of the request.
        self._display_name: Optional[str] = None
        # The external ID for the request that is immutable after creation and is used for tracking the request for the external system. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
        self._external_id: Optional[str] = None
        # Collection of history change events.
        self._history: Optional[List[subject_rights_request_history.SubjectRightsRequestHistory]] = None
        # Include all versions of the documents. By default, the current copies of the documents will be returned. If SharePoint sites have versioning enabled, including all versions will include the historical copies of the documents. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
        self._include_all_versions: Optional[bool] = None
        # Include content authored by the data subject. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
        self._include_authored_content: Optional[bool] = None
        # Insight about the request.
        self._insight: Optional[subject_rights_request_detail.SubjectRightsRequestDetail] = None
        # The date and time when the request is internally due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._internal_due_date_time: Optional[datetime] = None
        # Identity information for the entity that last modified the request.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The date and time when the request was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._last_modified_date_time: Optional[datetime] = None
        # The mailboxlocations property
        self._mailboxlocations: Optional[subject_rights_request_mailbox_location.SubjectRightsRequestMailboxLocation] = None
        # List of notes associated with the request.
        self._notes: Optional[List[authored_note.AuthoredNote]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Pause the request after estimate has finished. By default, the data estimate will run and then pause, allowing you to preview results and then select the option to retrieve data in the UI. You can set this property to false if you want it to perform the estimate and then automatically begin with the retrieval of the content. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
        self._pause_after_estimate: Optional[bool] = None
        # List of regulations that this request will fulfill.
        self._regulations: Optional[List[str]] = None
        # The sitelocations property
        self._sitelocations: Optional[subject_rights_request_site_location.SubjectRightsRequestSiteLocation] = None
        # Information about the different stages for the request.
        self._stages: Optional[List[subject_rights_request_stage_detail.SubjectRightsRequestStageDetail]] = None
        # The status of the request. Possible values are: active, closed, unknownFutureValue.
        self._status: Optional[subject_rights_request_status.SubjectRightsRequestStatus] = None
        # Information about the Microsoft Teams team that was created for the request.
        self._team: Optional[team.Team] = None
        # The type of the request. Possible values are: export, delete, access, tagForAction, unknownFutureValue.
        self._type: Optional[subject_rights_request_type.SubjectRightsRequestType] = None
    
    @property
    def content_query(self,) -> Optional[str]:
        """
        Gets the contentQuery property value. KQL based content query that should be used for search. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
        Returns: Optional[str]
        """
        return self._content_query
    
    @content_query.setter
    def content_query(self,value: Optional[str] = None) -> None:
        """
        Sets the contentQuery property value. KQL based content query that should be used for search. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
        Args:
            value: Value to set for the contentQuery property.
        """
        self._content_query = value
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. Identity information for the entity that created the request.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. Identity information for the entity that created the request.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the request was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the request was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubjectRightsRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SubjectRightsRequest()
    
    @property
    def data_subject(self,) -> Optional[data_subject.DataSubject]:
        """
        Gets the dataSubject property value. Information about the data subject.
        Returns: Optional[data_subject.DataSubject]
        """
        return self._data_subject
    
    @data_subject.setter
    def data_subject(self,value: Optional[data_subject.DataSubject] = None) -> None:
        """
        Sets the dataSubject property value. Information about the data subject.
        Args:
            value: Value to set for the dataSubject property.
        """
        self._data_subject = value
    
    @property
    def data_subject_type(self,) -> Optional[data_subject_type.DataSubjectType]:
        """
        Gets the dataSubjectType property value. The type of the data subject. Possible values are: customer, currentEmployee, formerEmployee, prospectiveEmployee, student, teacher, faculty, other, unknownFutureValue.
        Returns: Optional[data_subject_type.DataSubjectType]
        """
        return self._data_subject_type
    
    @data_subject_type.setter
    def data_subject_type(self,value: Optional[data_subject_type.DataSubjectType] = None) -> None:
        """
        Sets the dataSubjectType property value. The type of the data subject. Possible values are: customer, currentEmployee, formerEmployee, prospectiveEmployee, student, teacher, faculty, other, unknownFutureValue.
        Args:
            value: Value to set for the dataSubjectType property.
        """
        self._data_subject_type = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description for the request.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description for the request.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the request.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the request.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. The external ID for the request that is immutable after creation and is used for tracking the request for the external system. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. The external ID for the request that is immutable after creation and is used for tracking the request for the external system. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
        Args:
            value: Value to set for the externalId property.
        """
        self._external_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assigned_to": lambda n : setattr(self, 'assigned_to', n.get_object_value(identity.Identity)),
            "closed_date_time": lambda n : setattr(self, 'closed_date_time', n.get_datetime_value()),
            "content_query": lambda n : setattr(self, 'content_query', n.get_str_value()),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "data_subject": lambda n : setattr(self, 'data_subject', n.get_object_value(data_subject.DataSubject)),
            "data_subject_type": lambda n : setattr(self, 'data_subject_type', n.get_enum_value(data_subject_type.DataSubjectType)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "external_id": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(subject_rights_request_history.SubjectRightsRequestHistory)),
            "include_all_versions": lambda n : setattr(self, 'include_all_versions', n.get_bool_value()),
            "include_authored_content": lambda n : setattr(self, 'include_authored_content', n.get_bool_value()),
            "insight": lambda n : setattr(self, 'insight', n.get_object_value(subject_rights_request_detail.SubjectRightsRequestDetail)),
            "internal_due_date_time": lambda n : setattr(self, 'internal_due_date_time', n.get_datetime_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "mailboxlocations": lambda n : setattr(self, 'mailboxlocations', n.get_object_value(subject_rights_request_mailbox_location.SubjectRightsRequestMailboxLocation)),
            "notes": lambda n : setattr(self, 'notes', n.get_collection_of_object_values(authored_note.AuthoredNote)),
            "pause_after_estimate": lambda n : setattr(self, 'pause_after_estimate', n.get_bool_value()),
            "regulations": lambda n : setattr(self, 'regulations', n.get_collection_of_primitive_values(str)),
            "sitelocations": lambda n : setattr(self, 'sitelocations', n.get_object_value(subject_rights_request_site_location.SubjectRightsRequestSiteLocation)),
            "stages": lambda n : setattr(self, 'stages', n.get_collection_of_object_values(subject_rights_request_stage_detail.SubjectRightsRequestStageDetail)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(subject_rights_request_status.SubjectRightsRequestStatus)),
            "team": lambda n : setattr(self, 'team', n.get_object_value(team.Team)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(subject_rights_request_type.SubjectRightsRequestType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def history(self,) -> Optional[List[subject_rights_request_history.SubjectRightsRequestHistory]]:
        """
        Gets the history property value. Collection of history change events.
        Returns: Optional[List[subject_rights_request_history.SubjectRightsRequestHistory]]
        """
        return self._history
    
    @history.setter
    def history(self,value: Optional[List[subject_rights_request_history.SubjectRightsRequestHistory]] = None) -> None:
        """
        Sets the history property value. Collection of history change events.
        Args:
            value: Value to set for the history property.
        """
        self._history = value
    
    @property
    def include_all_versions(self,) -> Optional[bool]:
        """
        Gets the includeAllVersions property value. Include all versions of the documents. By default, the current copies of the documents will be returned. If SharePoint sites have versioning enabled, including all versions will include the historical copies of the documents. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
        Returns: Optional[bool]
        """
        return self._include_all_versions
    
    @include_all_versions.setter
    def include_all_versions(self,value: Optional[bool] = None) -> None:
        """
        Sets the includeAllVersions property value. Include all versions of the documents. By default, the current copies of the documents will be returned. If SharePoint sites have versioning enabled, including all versions will include the historical copies of the documents. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
        Args:
            value: Value to set for the includeAllVersions property.
        """
        self._include_all_versions = value
    
    @property
    def include_authored_content(self,) -> Optional[bool]:
        """
        Gets the includeAuthoredContent property value. Include content authored by the data subject. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
        Returns: Optional[bool]
        """
        return self._include_authored_content
    
    @include_authored_content.setter
    def include_authored_content(self,value: Optional[bool] = None) -> None:
        """
        Sets the includeAuthoredContent property value. Include content authored by the data subject. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
        Args:
            value: Value to set for the includeAuthoredContent property.
        """
        self._include_authored_content = value
    
    @property
    def insight(self,) -> Optional[subject_rights_request_detail.SubjectRightsRequestDetail]:
        """
        Gets the insight property value. Insight about the request.
        Returns: Optional[subject_rights_request_detail.SubjectRightsRequestDetail]
        """
        return self._insight
    
    @insight.setter
    def insight(self,value: Optional[subject_rights_request_detail.SubjectRightsRequestDetail] = None) -> None:
        """
        Sets the insight property value. Insight about the request.
        Args:
            value: Value to set for the insight property.
        """
        self._insight = value
    
    @property
    def internal_due_date_time(self,) -> Optional[datetime]:
        """
        Gets the internalDueDateTime property value. The date and time when the request is internally due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._internal_due_date_time
    
    @internal_due_date_time.setter
    def internal_due_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the internalDueDateTime property value. The date and time when the request is internally due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the internalDueDateTime property.
        """
        self._internal_due_date_time = value
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. Identity information for the entity that last modified the request.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. Identity information for the entity that last modified the request.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time when the request was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time when the request was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def mailboxlocations(self,) -> Optional[subject_rights_request_mailbox_location.SubjectRightsRequestMailboxLocation]:
        """
        Gets the mailboxlocations property value. The mailboxlocations property
        Returns: Optional[subject_rights_request_mailbox_location.SubjectRightsRequestMailboxLocation]
        """
        return self._mailboxlocations
    
    @mailboxlocations.setter
    def mailboxlocations(self,value: Optional[subject_rights_request_mailbox_location.SubjectRightsRequestMailboxLocation] = None) -> None:
        """
        Sets the mailboxlocations property value. The mailboxlocations property
        Args:
            value: Value to set for the mailboxlocations property.
        """
        self._mailboxlocations = value
    
    @property
    def notes(self,) -> Optional[List[authored_note.AuthoredNote]]:
        """
        Gets the notes property value. List of notes associated with the request.
        Returns: Optional[List[authored_note.AuthoredNote]]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[List[authored_note.AuthoredNote]] = None) -> None:
        """
        Sets the notes property value. List of notes associated with the request.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def pause_after_estimate(self,) -> Optional[bool]:
        """
        Gets the pauseAfterEstimate property value. Pause the request after estimate has finished. By default, the data estimate will run and then pause, allowing you to preview results and then select the option to retrieve data in the UI. You can set this property to false if you want it to perform the estimate and then automatically begin with the retrieval of the content. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
        Returns: Optional[bool]
        """
        return self._pause_after_estimate
    
    @pause_after_estimate.setter
    def pause_after_estimate(self,value: Optional[bool] = None) -> None:
        """
        Sets the pauseAfterEstimate property value. Pause the request after estimate has finished. By default, the data estimate will run and then pause, allowing you to preview results and then select the option to retrieve data in the UI. You can set this property to false if you want it to perform the estimate and then automatically begin with the retrieval of the content. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
        Args:
            value: Value to set for the pauseAfterEstimate property.
        """
        self._pause_after_estimate = value
    
    @property
    def regulations(self,) -> Optional[List[str]]:
        """
        Gets the regulations property value. List of regulations that this request will fulfill.
        Returns: Optional[List[str]]
        """
        return self._regulations
    
    @regulations.setter
    def regulations(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the regulations property value. List of regulations that this request will fulfill.
        Args:
            value: Value to set for the regulations property.
        """
        self._regulations = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("assignedTo", self.assigned_to)
        writer.write_datetime_value("closedDateTime", self.closed_date_time)
        writer.write_str_value("contentQuery", self.content_query)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("dataSubject", self.data_subject)
        writer.write_enum_value("dataSubjectType", self.data_subject_type)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("externalId", self.external_id)
        writer.write_collection_of_object_values("history", self.history)
        writer.write_bool_value("includeAllVersions", self.include_all_versions)
        writer.write_bool_value("includeAuthoredContent", self.include_authored_content)
        writer.write_object_value("insight", self.insight)
        writer.write_datetime_value("internalDueDateTime", self.internal_due_date_time)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("mailboxlocations", self.mailboxlocations)
        writer.write_collection_of_object_values("notes", self.notes)
        writer.write_bool_value("pauseAfterEstimate", self.pause_after_estimate)
        writer.write_collection_of_primitive_values("regulations", self.regulations)
        writer.write_object_value("sitelocations", self.sitelocations)
        writer.write_collection_of_object_values("stages", self.stages)
        writer.write_enum_value("status", self.status)
        writer.write_object_value("team", self.team)
        writer.write_enum_value("type", self.type)
    
    @property
    def sitelocations(self,) -> Optional[subject_rights_request_site_location.SubjectRightsRequestSiteLocation]:
        """
        Gets the sitelocations property value. The sitelocations property
        Returns: Optional[subject_rights_request_site_location.SubjectRightsRequestSiteLocation]
        """
        return self._sitelocations
    
    @sitelocations.setter
    def sitelocations(self,value: Optional[subject_rights_request_site_location.SubjectRightsRequestSiteLocation] = None) -> None:
        """
        Sets the sitelocations property value. The sitelocations property
        Args:
            value: Value to set for the sitelocations property.
        """
        self._sitelocations = value
    
    @property
    def stages(self,) -> Optional[List[subject_rights_request_stage_detail.SubjectRightsRequestStageDetail]]:
        """
        Gets the stages property value. Information about the different stages for the request.
        Returns: Optional[List[subject_rights_request_stage_detail.SubjectRightsRequestStageDetail]]
        """
        return self._stages
    
    @stages.setter
    def stages(self,value: Optional[List[subject_rights_request_stage_detail.SubjectRightsRequestStageDetail]] = None) -> None:
        """
        Sets the stages property value. Information about the different stages for the request.
        Args:
            value: Value to set for the stages property.
        """
        self._stages = value
    
    @property
    def status(self,) -> Optional[subject_rights_request_status.SubjectRightsRequestStatus]:
        """
        Gets the status property value. The status of the request. Possible values are: active, closed, unknownFutureValue.
        Returns: Optional[subject_rights_request_status.SubjectRightsRequestStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[subject_rights_request_status.SubjectRightsRequestStatus] = None) -> None:
        """
        Sets the status property value. The status of the request. Possible values are: active, closed, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def team(self,) -> Optional[team.Team]:
        """
        Gets the team property value. Information about the Microsoft Teams team that was created for the request.
        Returns: Optional[team.Team]
        """
        return self._team
    
    @team.setter
    def team(self,value: Optional[team.Team] = None) -> None:
        """
        Sets the team property value. Information about the Microsoft Teams team that was created for the request.
        Args:
            value: Value to set for the team property.
        """
        self._team = value
    
    @property
    def type(self,) -> Optional[subject_rights_request_type.SubjectRightsRequestType]:
        """
        Gets the type property value. The type of the request. Possible values are: export, delete, access, tagForAction, unknownFutureValue.
        Returns: Optional[subject_rights_request_type.SubjectRightsRequestType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[subject_rights_request_type.SubjectRightsRequestType] = None) -> None:
        """
        Sets the type property value. The type of the request. Possible values are: export, delete, access, tagForAction, unknownFutureValue.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

